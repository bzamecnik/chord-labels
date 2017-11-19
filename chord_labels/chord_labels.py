from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from antlr4.error.ErrorListener import ErrorListener

from chord_labels.parser.ChordLabelLexer import ChordLabelLexer
from chord_labels.parser.ChordLabelParser import ChordLabelParser
from chord_labels.parser.ChordLabelListener import ChordLabelListener

def parse_chord(label):
    """
    Parses a string chord label from a string form to ChorlLabel instance
    (containing a set of pitch classes, root, bass).

    Examples:
    ```
    from chord_labels import parse_chord

    chord = parse_chord("C:maj7")
    assert chord.tones == [0, 4, 7, 11]
    assert chord.tones_binary == [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1]

    assert parse_chord("F#").root == 6

    assert parse_chord("C#/5").bass == 8
    ```
    """
    lexer = ChordLabelLexer(InputStream(label))
    stream = CommonTokenStream(lexer)
    parser = ChordLabelParser(stream)
    parser._listeners = [ChordErrorListener()]
    chordContext = parser.chord()
    walker = ParseTreeWalker()
    listener = ChordLabelReader()
    walker.walk(listener, chordContext)
    return listener.chord_label

OCTAVE_SIZE = 12

DEFAULT_SHORTHAND = "maj"
# upper tones, except for the root
SHORTHANDS = {
    "maj": set([4, 7]),
    "min": set([3, 7]),
    "dim": set([3, 6]),
    "aug": set([4, 8]),
    "maj7": set([4, 7, 11]),
    "min7": set([3, 7, 10]),
    "dim7": set([3, 6, 9]),
    "hdim7": set([3, 6, 10]),
    "minmaj7": set([3, 7, 11]),
    "maj6": set([4, 7, 9]),
    "min6": set([3, 7, 9]),
    "maj9": set([4, 7, 11, 2]),
    "min9": set([3, 7, 10, 2]),
    "sus4": set([5, 7]),
    "sus2": set([2, 7]),
    "7": set([4, 7, 10]),
    "9": set([4, 7, 10, 2]),
    "11": set([4, 7, 10, 2, 5]),
    "13": set([4, 7, 10, 2, 5, 9]),
}
PITCH_CLASS_FROM_NAME = {
    "A": 9,
    "B": 11,
    "C": 0,
    "D": 2,
    "E": 4,
    "F": 5,
    "G": 7,
}
# diatonic scale interval -> pitch class
PITCH_CLASS_FROM_INTERVAL = {
    1: 0,
    2: 2,
    3: 4,
    4: 5,
    5: 7,
    6: 9,
    7: 11,
}
PITCH_CLASS_FROM_MODIFIER = {
    "b": OCTAVE_SIZE - 1,
    "#": 1,
}
PITCH_CLASS_NAMES = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']

class ChordLabel:
    # tones: set - absolute pitch classes
    # root: int - absolute pitch class
    # bass: int - absolute pitch class
    # title: str
    def __init__(self, tones, root, bass, title=""):
        tones_set = set(tones) if not isinstance(tones, set) else tones
        self.tones = sorted(tones_set)
        self.root = root
        self.bass = bass
        self.title = title
        # eg. [0, 4, 7, 11] - > [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1]
        self.tones_binary = [int(i in tones) for i in range(OCTAVE_SIZE)]

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(self, other.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __repr__(self):
        return "ChordLabel({}, {}, {}, {})".format(
            repr(self.tones), repr(self.root), repr(self.bass), repr(self.title))

class ChordLabelReader(ChordLabelListener):

    def __init__(self):
        # Currently processed pitch class. For root tone it is absolute, for
        # components (including the bass tone) it is relative to the root.
        #
        # This variable might be modified by the diatonic natural tone symbol (for
        # root), diatonic interval symbol (for further components) and flat/sharp
        # modifiers.
        self.pitch_class = 0
        # Indicates whether the current component should be added (default) or
        # removed as marked by an asterisk (*).
        self.should_add_component = True
        self.any_component_specified = False
        self.abs_root = 0
        self.relative_tones = set()
        self.relative_bass = 0
        self.is_empty_chord = True
        # the output
        self.chord_label = None

    # ctx: ChordLabelParser.ModifierContext
    def enterModifier(self, ctx):
        self.pitch_class = self._pitch_class(self.pitch_class + PITCH_CLASS_FROM_MODIFIER[ctx.getText()])

    # ctx: ChordLabelParser.ShorthandContext
    def enterShorthand(self, ctx):
        self.relative_tones |= SHORTHANDS[ctx.getText()]
        self.any_component_specified = True

    # ctx: ChordLabelParser.RootContext
    def exitRoot(self, ctx):
        self.abs_root = self.pitch_class
        self.relative_tones.add(0)

    # ctx: ChordLabelParser.BassContext
    def enterBass(self, ctx):
        self.pitch_class = 0

    # ctx: ChordLabelParser.BassContext
    def exitBass(self, ctx):
        self.relative_bass = self.pitch_class
        self.relative_tones.add(self.relative_bass)

    # ctx: ChordLabelParser.NaturalContext
    def enterNatural(self, ctx):
        self.is_empty_chord = False
        self.pitch_class = PITCH_CLASS_FROM_NAME[ctx.getText()]

    # ctx: ComponentContext
    def enterComponent(self, ctx):
        self.pitch_class = 0
        self.should_add_component = True
        self.any_component_specified = True

    # ctx: ComponentContext
    def exitComponent(self, ctx):
        if self.should_add_component:
            self.relative_tones.add(self.pitch_class)
        else:
            self.relative_tones.remove(self.pitch_class)

    # ctx: IntervalContext
    def enterInterval(self, ctx):
        interval = int(ctx.getText())
        # normalize diatonic interval to [1; 7]
        normalized_interval = ((interval - 1) % 7) + 1
        self.pitch_class = self._pitch_class(self.pitch_class + PITCH_CLASS_FROM_INTERVAL[normalized_interval])

    # ctx: MissingContext
    def enterMissing(self, ctx):
        self.should_add_component = False

    # Resets the chord state.
    # ctx: ChordLabelParser.ChordContext
    def enterChord(self, ctx):
        self.pitch_class = 0
        self.should_add_component = True
        self.any_component_specified = False
        self.abs_root = 0
        self.relative_tones = set()
        self.relative_bass = 0
        self.is_empty_chord = True

    # ctx: ChordLabelParser.ChordContext
    def exitChord(self, ctx):
        if not self.is_empty_chord and not self.any_component_specified:
            self.relative_tones |= SHORTHANDS[DEFAULT_SHORTHAND]

        # convert all pitch classes from relative to absolute
        tones = [self._pitch_class(tone + self.abs_root) for tone in self.relative_tones]
        root = self._pitch_class(self.abs_root)
        bass = self._pitch_class(self.relative_bass + root)
        title = ctx.getText()
        self.chord_label = ChordLabel(tones, root, bass, title)

    def _pitch_class(self, pitch):
        return pitch % OCTAVE_SIZE

class ChordException(Exception):
    pass

class ChordErrorListener(ErrorListener):
    def __init__(self):
        super(ChordErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ChordException("Syntax error: recognizer: {}, offendingSymbol: {}, line: {}, column: {}, msg: {}, e: {}".format(
            recognizer, offendingSymbol, line, column, msg, e))

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        raise ChordException("Ambiguity: recognizer: {}, dfs: {}, startIndex: {}, stopIndex: {}, ambigAlts: {}, configs: {}".format(
            recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs))

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        raise ChordException("Ambiguity: recognizer: {}, dfs: {}, startIndex: {}, stopIndex: {}, conflictingAlts: {}, configs: {}".format(
            recognizer, dfa, startIndex, stopIndex, exact, conflictingAlts, configs))

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        raise ChordException("Ambiguity: recognizer: {}, dfa: {}, startIndex: {}, stopIndex: {}, prediction: {}, configs: {}".format(
            recognizer, dfa, startIndex, stopIndex, prediction, configss))
