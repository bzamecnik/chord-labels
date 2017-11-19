/**
 * Grammar for chord labels (ANTLR 4).
 *
 * Harte, C. et al. (2005)
 * Symbolic representation of musical chords: a proposed syntax for text
 * annotations. Proceedings of 6th International Conference on Music
 * Information Retrieval.
 *
 * http://ismir2005.ismir.net/proceedings/1080.pdf
 *
 * Syntax of Chord Notation in Backus-Naur Form:
 *
 * <chord> ::=   <root> ":" <shorthand> ["("<degree-list>")"]["/"<degree>]
 *             | <root> ":" "("<degree-list>")" ["/"<degree>]
 *             | <root> ["/"<degree>] | "N"
 * <root>         ::= <natural> | <root> <modifier>
 * <natural>      ::= A|B|C|D|E|F|G
 * <modifier>     ::= b|#
 * <degree-list>  ::=  ["*"] <degree> ["," <degree-list>]
 * <degree>       ::= <interval> | <modifier> <degree>
 * <interval>     ::= 1|2|3|4|5|6|7|8|9|10|11|12|13
 * <shorthand>    ::= maj|min|dim|aug|maj7|min7|7|dim7|hdim7
 *                    |minmaj7|maj6|min6|9|maj9|min9|sus4
 */

grammar ChordLabel;

chord: root (SEPARATOR (components | shorthand components?))? bass?	| NO_CHORD;
root: natural modifier*;
natural: NATURAL;
modifier: FLAT | SHARP;
components: '(' component (',' component)* ')';
component: missing? degree;
missing: '*';
degree: modifier* interval;
interval: I_1 | I_2 | I_3 | I_4 | I_5 | I_6 | I_7 | I_8 | I_9 | I_10 | I_11 | I_12 | I_13;
bass: ('/' degree);
// note: we have to share the symbols with INTERVAL to prevent conflicts
shorthand:
  // original shorthands from paper
  'maj' | 'min' | 'dim' | 'aug'
  | 'maj7' | 'min7' | I_7 | 'dim7' | 'hdim7' | 'minmaj7'
  | 'maj6' | 'min6'
  | I_9 | 'maj9' | 'min9'
  | 'sus4'
  // extra shorthands (not in the original paper, but appearing in practice)
  // C:11 = C:9(11)
  // C:13 = C:9(11,13)
  // C:sus2 = C:(2,5)
  | I_11 | I_13 | 'sus2';

NATURAL: ('A'..'G');
FLAT: 'b';
SHARP: '#';
I_1: '1';
I_2: '2';
I_3: '3';
I_4: '4';
I_5: '5';
I_6: '6';
I_7: '7';
I_8: '8';
I_9: '9';
I_10: '10';
I_11: '11';
I_12: '12';
I_13: '13';
NO_CHORD: 'N';
SEPARATOR: ':';
