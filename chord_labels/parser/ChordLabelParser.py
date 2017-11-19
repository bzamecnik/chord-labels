# Generated from ChordLabel.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3(")
        buf.write("V\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2\3\2")
        buf.write("\3\2\5\2\36\n\2\5\2 \n\2\5\2\"\n\2\3\2\5\2%\n\2\3\2\5")
        buf.write("\2(\n\2\3\3\3\3\7\3,\n\3\f\3\16\3/\13\3\3\4\3\4\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\7\69\n\6\f\6\16\6<\13\6\3\6\3\6\3\7")
        buf.write("\5\7A\n\7\3\7\3\7\3\b\3\b\3\t\7\tH\n\t\f\t\16\tK\13\t")
        buf.write("\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\2\2\r\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\2\5\3\2\30\31\3\2\32&\7\2\b\26")
        buf.write("  \"\"$$&&\2S\2\'\3\2\2\2\4)\3\2\2\2\6\60\3\2\2\2\b\62")
        buf.write("\3\2\2\2\n\64\3\2\2\2\f@\3\2\2\2\16D\3\2\2\2\20I\3\2\2")
        buf.write("\2\22N\3\2\2\2\24P\3\2\2\2\26S\3\2\2\2\30!\5\4\3\2\31")
        buf.write("\37\7(\2\2\32 \5\n\6\2\33\35\5\26\f\2\34\36\5\n\6\2\35")
        buf.write("\34\3\2\2\2\35\36\3\2\2\2\36 \3\2\2\2\37\32\3\2\2\2\37")
        buf.write("\33\3\2\2\2 \"\3\2\2\2!\31\3\2\2\2!\"\3\2\2\2\"$\3\2\2")
        buf.write("\2#%\5\24\13\2$#\3\2\2\2$%\3\2\2\2%(\3\2\2\2&(\7\'\2\2")
        buf.write("\'\30\3\2\2\2\'&\3\2\2\2(\3\3\2\2\2)-\5\6\4\2*,\5\b\5")
        buf.write("\2+*\3\2\2\2,/\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\5\3\2\2\2")
        buf.write("/-\3\2\2\2\60\61\7\27\2\2\61\7\3\2\2\2\62\63\t\2\2\2\63")
        buf.write("\t\3\2\2\2\64\65\7\3\2\2\65:\5\f\7\2\66\67\7\4\2\2\67")
        buf.write("9\5\f\7\28\66\3\2\2\29<\3\2\2\2:8\3\2\2\2:;\3\2\2\2;=")
        buf.write("\3\2\2\2<:\3\2\2\2=>\7\5\2\2>\13\3\2\2\2?A\5\16\b\2@?")
        buf.write("\3\2\2\2@A\3\2\2\2AB\3\2\2\2BC\5\20\t\2C\r\3\2\2\2DE\7")
        buf.write("\6\2\2E\17\3\2\2\2FH\5\b\5\2GF\3\2\2\2HK\3\2\2\2IG\3\2")
        buf.write("\2\2IJ\3\2\2\2JL\3\2\2\2KI\3\2\2\2LM\5\22\n\2M\21\3\2")
        buf.write("\2\2NO\t\3\2\2O\23\3\2\2\2PQ\7\7\2\2QR\5\20\t\2R\25\3")
        buf.write("\2\2\2ST\t\4\2\2T\27\3\2\2\2\13\35\37!$\'-:@I")
        return buf.getvalue()


class ChordLabelParser ( Parser ):

    grammarFileName = "ChordLabel.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "'*'", "'/'", "'maj'", 
                     "'min'", "'dim'", "'aug'", "'maj7'", "'min7'", "'dim7'", 
                     "'hdim7'", "'minmaj7'", "'maj6'", "'min6'", "'maj9'", 
                     "'min9'", "'sus4'", "'sus2'", "<INVALID>", "'b'", "'#'", 
                     "'1'", "'2'", "'3'", "'4'", "'5'", "'6'", "'7'", "'8'", 
                     "'9'", "'10'", "'11'", "'12'", "'13'", "'N'", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NATURAL", "FLAT", "SHARP", "I_1", "I_2", 
                      "I_3", "I_4", "I_5", "I_6", "I_7", "I_8", "I_9", "I_10", 
                      "I_11", "I_12", "I_13", "NO_CHORD", "SEPARATOR" ]

    RULE_chord = 0
    RULE_root = 1
    RULE_natural = 2
    RULE_modifier = 3
    RULE_components = 4
    RULE_component = 5
    RULE_missing = 6
    RULE_degree = 7
    RULE_interval = 8
    RULE_bass = 9
    RULE_shorthand = 10

    ruleNames =  [ "chord", "root", "natural", "modifier", "components", 
                   "component", "missing", "degree", "interval", "bass", 
                   "shorthand" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    NATURAL=21
    FLAT=22
    SHARP=23
    I_1=24
    I_2=25
    I_3=26
    I_4=27
    I_5=28
    I_6=29
    I_7=30
    I_8=31
    I_9=32
    I_10=33
    I_11=34
    I_12=35
    I_13=36
    NO_CHORD=37
    SEPARATOR=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ChordContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def root(self):
            return self.getTypedRuleContext(ChordLabelParser.RootContext,0)


        def SEPARATOR(self):
            return self.getToken(ChordLabelParser.SEPARATOR, 0)

        def bass(self):
            return self.getTypedRuleContext(ChordLabelParser.BassContext,0)


        def components(self):
            return self.getTypedRuleContext(ChordLabelParser.ComponentsContext,0)


        def shorthand(self):
            return self.getTypedRuleContext(ChordLabelParser.ShorthandContext,0)


        def NO_CHORD(self):
            return self.getToken(ChordLabelParser.NO_CHORD, 0)

        def getRuleIndex(self):
            return ChordLabelParser.RULE_chord

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChord" ):
                listener.enterChord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChord" ):
                listener.exitChord(self)




    def chord(self):

        localctx = ChordLabelParser.ChordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_chord)
        self._la = 0 # Token type
        try:
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ChordLabelParser.NATURAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.root()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ChordLabelParser.SEPARATOR:
                    self.state = 23
                    self.match(ChordLabelParser.SEPARATOR)
                    self.state = 29
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [ChordLabelParser.T__0]:
                        self.state = 24
                        self.components()
                        pass
                    elif token in [ChordLabelParser.T__5, ChordLabelParser.T__6, ChordLabelParser.T__7, ChordLabelParser.T__8, ChordLabelParser.T__9, ChordLabelParser.T__10, ChordLabelParser.T__11, ChordLabelParser.T__12, ChordLabelParser.T__13, ChordLabelParser.T__14, ChordLabelParser.T__15, ChordLabelParser.T__16, ChordLabelParser.T__17, ChordLabelParser.T__18, ChordLabelParser.T__19, ChordLabelParser.I_7, ChordLabelParser.I_9, ChordLabelParser.I_11, ChordLabelParser.I_13]:
                        self.state = 25
                        self.shorthand()
                        self.state = 27
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==ChordLabelParser.T__0:
                            self.state = 26
                            self.components()


                        pass
                    else:
                        raise NoViableAltException(self)



                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ChordLabelParser.T__4:
                    self.state = 33
                    self.bass()


                pass
            elif token in [ChordLabelParser.NO_CHORD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.match(ChordLabelParser.NO_CHORD)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def natural(self):
            return self.getTypedRuleContext(ChordLabelParser.NaturalContext,0)


        def modifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChordLabelParser.ModifierContext)
            else:
                return self.getTypedRuleContext(ChordLabelParser.ModifierContext,i)


        def getRuleIndex(self):
            return ChordLabelParser.RULE_root

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoot" ):
                listener.enterRoot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoot" ):
                listener.exitRoot(self)




    def root(self):

        localctx = ChordLabelParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.natural()
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ChordLabelParser.FLAT or _la==ChordLabelParser.SHARP:
                self.state = 40
                self.modifier()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NaturalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NATURAL(self):
            return self.getToken(ChordLabelParser.NATURAL, 0)

        def getRuleIndex(self):
            return ChordLabelParser.RULE_natural

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNatural" ):
                listener.enterNatural(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNatural" ):
                listener.exitNatural(self)




    def natural(self):

        localctx = ChordLabelParser.NaturalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_natural)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(ChordLabelParser.NATURAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ModifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLAT(self):
            return self.getToken(ChordLabelParser.FLAT, 0)

        def SHARP(self):
            return self.getToken(ChordLabelParser.SHARP, 0)

        def getRuleIndex(self):
            return ChordLabelParser.RULE_modifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModifier" ):
                listener.enterModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModifier" ):
                listener.exitModifier(self)




    def modifier(self):

        localctx = ChordLabelParser.ModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_modifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            _la = self._input.LA(1)
            if not(_la==ChordLabelParser.FLAT or _la==ChordLabelParser.SHARP):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ComponentsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def component(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChordLabelParser.ComponentContext)
            else:
                return self.getTypedRuleContext(ChordLabelParser.ComponentContext,i)


        def getRuleIndex(self):
            return ChordLabelParser.RULE_components

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComponents" ):
                listener.enterComponents(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComponents" ):
                listener.exitComponents(self)




    def components(self):

        localctx = ChordLabelParser.ComponentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_components)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(ChordLabelParser.T__0)
            self.state = 51
            self.component()
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ChordLabelParser.T__1:
                self.state = 52
                self.match(ChordLabelParser.T__1)
                self.state = 53
                self.component()
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 59
            self.match(ChordLabelParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ComponentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def degree(self):
            return self.getTypedRuleContext(ChordLabelParser.DegreeContext,0)


        def missing(self):
            return self.getTypedRuleContext(ChordLabelParser.MissingContext,0)


        def getRuleIndex(self):
            return ChordLabelParser.RULE_component

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComponent" ):
                listener.enterComponent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComponent" ):
                listener.exitComponent(self)




    def component(self):

        localctx = ChordLabelParser.ComponentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_component)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ChordLabelParser.T__3:
                self.state = 61
                self.missing()


            self.state = 64
            self.degree()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MissingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ChordLabelParser.RULE_missing

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMissing" ):
                listener.enterMissing(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMissing" ):
                listener.exitMissing(self)




    def missing(self):

        localctx = ChordLabelParser.MissingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_missing)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(ChordLabelParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DegreeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interval(self):
            return self.getTypedRuleContext(ChordLabelParser.IntervalContext,0)


        def modifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChordLabelParser.ModifierContext)
            else:
                return self.getTypedRuleContext(ChordLabelParser.ModifierContext,i)


        def getRuleIndex(self):
            return ChordLabelParser.RULE_degree

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDegree" ):
                listener.enterDegree(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDegree" ):
                listener.exitDegree(self)




    def degree(self):

        localctx = ChordLabelParser.DegreeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_degree)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ChordLabelParser.FLAT or _la==ChordLabelParser.SHARP:
                self.state = 68
                self.modifier()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
            self.interval()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IntervalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def I_1(self):
            return self.getToken(ChordLabelParser.I_1, 0)

        def I_2(self):
            return self.getToken(ChordLabelParser.I_2, 0)

        def I_3(self):
            return self.getToken(ChordLabelParser.I_3, 0)

        def I_4(self):
            return self.getToken(ChordLabelParser.I_4, 0)

        def I_5(self):
            return self.getToken(ChordLabelParser.I_5, 0)

        def I_6(self):
            return self.getToken(ChordLabelParser.I_6, 0)

        def I_7(self):
            return self.getToken(ChordLabelParser.I_7, 0)

        def I_8(self):
            return self.getToken(ChordLabelParser.I_8, 0)

        def I_9(self):
            return self.getToken(ChordLabelParser.I_9, 0)

        def I_10(self):
            return self.getToken(ChordLabelParser.I_10, 0)

        def I_11(self):
            return self.getToken(ChordLabelParser.I_11, 0)

        def I_12(self):
            return self.getToken(ChordLabelParser.I_12, 0)

        def I_13(self):
            return self.getToken(ChordLabelParser.I_13, 0)

        def getRuleIndex(self):
            return ChordLabelParser.RULE_interval

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterval" ):
                listener.enterInterval(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterval" ):
                listener.exitInterval(self)




    def interval(self):

        localctx = ChordLabelParser.IntervalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_interval)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ChordLabelParser.I_1) | (1 << ChordLabelParser.I_2) | (1 << ChordLabelParser.I_3) | (1 << ChordLabelParser.I_4) | (1 << ChordLabelParser.I_5) | (1 << ChordLabelParser.I_6) | (1 << ChordLabelParser.I_7) | (1 << ChordLabelParser.I_8) | (1 << ChordLabelParser.I_9) | (1 << ChordLabelParser.I_10) | (1 << ChordLabelParser.I_11) | (1 << ChordLabelParser.I_12) | (1 << ChordLabelParser.I_13))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BassContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def degree(self):
            return self.getTypedRuleContext(ChordLabelParser.DegreeContext,0)


        def getRuleIndex(self):
            return ChordLabelParser.RULE_bass

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBass" ):
                listener.enterBass(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBass" ):
                listener.exitBass(self)




    def bass(self):

        localctx = ChordLabelParser.BassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_bass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(ChordLabelParser.T__4)
            self.state = 79
            self.degree()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ShorthandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def I_7(self):
            return self.getToken(ChordLabelParser.I_7, 0)

        def I_9(self):
            return self.getToken(ChordLabelParser.I_9, 0)

        def I_11(self):
            return self.getToken(ChordLabelParser.I_11, 0)

        def I_13(self):
            return self.getToken(ChordLabelParser.I_13, 0)

        def getRuleIndex(self):
            return ChordLabelParser.RULE_shorthand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShorthand" ):
                listener.enterShorthand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShorthand" ):
                listener.exitShorthand(self)




    def shorthand(self):

        localctx = ChordLabelParser.ShorthandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_shorthand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ChordLabelParser.T__5) | (1 << ChordLabelParser.T__6) | (1 << ChordLabelParser.T__7) | (1 << ChordLabelParser.T__8) | (1 << ChordLabelParser.T__9) | (1 << ChordLabelParser.T__10) | (1 << ChordLabelParser.T__11) | (1 << ChordLabelParser.T__12) | (1 << ChordLabelParser.T__13) | (1 << ChordLabelParser.T__14) | (1 << ChordLabelParser.T__15) | (1 << ChordLabelParser.T__16) | (1 << ChordLabelParser.T__17) | (1 << ChordLabelParser.T__18) | (1 << ChordLabelParser.T__19) | (1 << ChordLabelParser.I_7) | (1 << ChordLabelParser.I_9) | (1 << ChordLabelParser.I_11) | (1 << ChordLabelParser.I_13))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





