# chord-labels

MIREX-style chord labels parser in Python 3 (based on ANTLR)

It allows to parse symbolic chord labels defined in [1] into [pitch class sets](http://en.wikipedia.org/wiki/Set_theory_(music)).

For example:

- `C` into `[0, 4, 7]`.
- `C:(b3,5,b7)` into `[0, 3, 7, 10]`.
- `D:min` into `[2, 5, 9]`.
- `Eb:min7(9)/5` into `[3, 5, 6, 10, 1]`.

## How to build and use?

Install for using:

```shell
$ pip install chord-labels
```

### Basic usage examples

TL;DR:

```python
from chord_labels import parse_chord
assert parse_chord("C:maj7").tones == [0, 4, 7, 11]
```

You can parse one chord at time. The result of `parse_chord()` is an instance of the `ChordLabel` class. It provides a few properties:

- `tones` - set of absolute pitch classes (C is 0)
- `binary_tones` - binary list of absolute pitch classes
- `root` - absolute pitch class of the root tone
- `bass` - absolute pitch class of the bass tone (behind slash)

```python
from chord_labels import parse_chord, ChordLabel

chord = parse_chord("C:maj7")

# pitch classes, root, bass, label
assert chord == ChordLabel([0, 4, 7, 11], 0, 0, 'C:maj7')

assert chord.tones == [0, 4, 7, 11]
assert chord.tones_binary == [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1]

assert parse_chord("F#").root == 6

assert parse_chord("C#/5").bass == 8
```

### Development

Install for development:

```shell
$ git clone https://github.com/bzamecnik/chord-labels.git
$ pip install -e chord-labels
```

The lexer/parser code is generated from ANTLR grammar to Python. You need `antlr4` installed.

```shell
# Ubuntu:
$ sudo apt install antlr4
# OS X:
$ brew install antlr
```

```shell
# regenerate the files
$ python setup.py antlr
```

## Syntax

- The root tone is written as the natural tone name (A, B, C, D, E, D, G) with optional suffix modifiers (flat - `b`, sharp - `#`).
	- Eg. `C`, `Eb`, `G#`, `Cbb#b`
- After the separator (:) there are other components of the chord written as numeric diatonic intervals relative to the root (with optional one or more prefix modifiers). Eg. (2, b3, 3, 4, b5, 5, #5, 6, bb7, b7, 7). The intervals can span into the second octave (eg. b9, 9, #9, 11, 13). The components are in parentheses and separated by a comma. The root tone already defined the tonic (the 1 component).
	- Eg. `C:(3,5)`, `D:(b3,b5,b7)`, `G:(3,5,b7,9,11,13)`
- For some common chords there are "shorthands" - pre-defined sets of components identified by name. A shorthand is optional and can be combined with explicit components. Generally either a shorthand or a list of components must be present after the separator.
	- Eg. `C:min` = `C:(b3,5)`, `C:maj7` = `C:(4,5,7)`
	- Pre-defined shorthands:
		- maj = (3,5)
		- min = (b3,5)
		- dim = (b3,b5)
		- aug = (3,#5)
		- maj7 = (3,5,7)
		- min7 = (b3,5,b7)
		- 7 = (3,5,b7)
		- dim7 = (b3,b5,bb7)
		- hdim7 = (b3,b5,b7)
		- minmaj7 = (b3,5,7)
		- maj6 = (3,5,6)
		- min6 = (b3,5,6)
		- 9 = (3,5,b7,9)
		- maj9 = (3,5,7,9)
		- min9 = (b3,5,b7,9)
		- sus4 = (4,5)
- In order to exclude some tone from the shorthand, we can prefix it with an asterisk (`*`).
	- Eg. `C:7(*5)` = `C:(3,b7)`
- The syntax allows to specify some concrete inversion of the chord, ie. some ordering of the pitch class set. In particular, there can be some explicit bass tone. Similarly to common notation it marked is optionally at the end as an relative interval with modified after a slash.
	- Eg. `C:maj/3` - bass tone is the third
- As a syntax sugar, a lonely root tone symbol (with no components or a shorthand) is considered to denote the major chord.
	- Eg. `C` = `C:maj` = `C:(3,5)`

### API

The API is currently not stable and might change without any notification.

## Author & License

- Bohumir Zamecnik ([@bzamecnik](https://twitter.com/bzamecnik))
- License: MIT (see the [LICENSE](LICENSE) file)

Enjoy and feel free to use and talk about any enhancements/bugs.

Originally this was implemented in Java [chord-labels-java](https://github.com/bzamecnik/chord-labels-java).

## References

- [1] Harte, C. et al. (2005). [Symbolic representation of musical chords:
a proposed syntax for text annotations](http://ismir2005.ismir.net/proceedings/1080.pdf). Proceedings of 6th International
Conference on Music Information Retrieval.
- [2] Harte, C. (2010). [Towards Automatic Extraction of Harmony Information from Music Signals](https://code.soundsoftware.ac.uk/attachments/download/330/chris_harte_phd_thesis.pdf). PhD. thesis
- [3] [Ground-truth chord labels for Beatles album annotated by Chris Harte](http://www.ee.columbia.edu/~dpwe/e4896/practicals.html#prac10)
- [4] [Beatles Annotations](http://isophonics.net/content/reference-annotations-beatles) dataset
