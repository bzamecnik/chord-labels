# Generated from ChordLabel.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ChordLabelParser import ChordLabelParser
else:
    from ChordLabelParser import ChordLabelParser

# This class defines a complete listener for a parse tree produced by ChordLabelParser.
class ChordLabelListener(ParseTreeListener):

    # Enter a parse tree produced by ChordLabelParser#chord.
    def enterChord(self, ctx:ChordLabelParser.ChordContext):
        pass

    # Exit a parse tree produced by ChordLabelParser#chord.
    def exitChord(self, ctx:ChordLabelParser.ChordContext):
        pass


    # Enter a parse tree produced by ChordLabelParser#root.
    def enterRoot(self, ctx:ChordLabelParser.RootContext):
        pass

    # Exit a parse tree produced by ChordLabelParser#root.
    def exitRoot(self, ctx:ChordLabelParser.RootContext):
        pass


    # Enter a parse tree produced by ChordLabelParser#natural.
    def enterNatural(self, ctx:ChordLabelParser.NaturalContext):
        pass

    # Exit a parse tree produced by ChordLabelParser#natural.
    def exitNatural(self, ctx:ChordLabelParser.NaturalContext):
        pass


    # Enter a parse tree produced by ChordLabelParser#modifier.
    def enterModifier(self, ctx:ChordLabelParser.ModifierContext):
        pass

    # Exit a parse tree produced by ChordLabelParser#modifier.
    def exitModifier(self, ctx:ChordLabelParser.ModifierContext):
        pass


    # Enter a parse tree produced by ChordLabelParser#components.
    def enterComponents(self, ctx:ChordLabelParser.ComponentsContext):
        pass

    # Exit a parse tree produced by ChordLabelParser#components.
    def exitComponents(self, ctx:ChordLabelParser.ComponentsContext):
        pass


    # Enter a parse tree produced by ChordLabelParser#component.
    def enterComponent(self, ctx:ChordLabelParser.ComponentContext):
        pass

    # Exit a parse tree produced by ChordLabelParser#component.
    def exitComponent(self, ctx:ChordLabelParser.ComponentContext):
        pass


    # Enter a parse tree produced by ChordLabelParser#missing.
    def enterMissing(self, ctx:ChordLabelParser.MissingContext):
        pass

    # Exit a parse tree produced by ChordLabelParser#missing.
    def exitMissing(self, ctx:ChordLabelParser.MissingContext):
        pass


    # Enter a parse tree produced by ChordLabelParser#degree.
    def enterDegree(self, ctx:ChordLabelParser.DegreeContext):
        pass

    # Exit a parse tree produced by ChordLabelParser#degree.
    def exitDegree(self, ctx:ChordLabelParser.DegreeContext):
        pass


    # Enter a parse tree produced by ChordLabelParser#interval.
    def enterInterval(self, ctx:ChordLabelParser.IntervalContext):
        pass

    # Exit a parse tree produced by ChordLabelParser#interval.
    def exitInterval(self, ctx:ChordLabelParser.IntervalContext):
        pass


    # Enter a parse tree produced by ChordLabelParser#bass.
    def enterBass(self, ctx:ChordLabelParser.BassContext):
        pass

    # Exit a parse tree produced by ChordLabelParser#bass.
    def exitBass(self, ctx:ChordLabelParser.BassContext):
        pass


    # Enter a parse tree produced by ChordLabelParser#shorthand.
    def enterShorthand(self, ctx:ChordLabelParser.ShorthandContext):
        pass

    # Exit a parse tree produced by ChordLabelParser#shorthand.
    def exitShorthand(self, ctx:ChordLabelParser.ShorthandContext):
        pass


