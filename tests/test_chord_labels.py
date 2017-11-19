from chord_labels import parse_chord, ChordLabel

def test_no_chord():
    assert parse_chord('N') == ChordLabel([], 0, 0, 'N')

def test_basic_c_chord():
    assert parse_chord('C') == ChordLabel([0, 4, 7], 0, 0, 'C')
    assert parse_chord('C:maj') == ChordLabel([0, 4, 7], 0, 0, 'C:maj')
    assert parse_chord('C:(3,5)') == ChordLabel([0, 4, 7], 0, 0, 'C:(3,5)')

def test_c_sharp_maj7_chord():
    assert parse_chord('C#:maj7') == ChordLabel([1, 5, 8, 0], 1, 1, 'C#:maj7')

def test_e7_chord():
    assert parse_chord('E:7') == ChordLabel([4, 8, 11, 2], 4, 4, 'E:7')

def test_slash_chord():
    assert parse_chord('Gb/3') == ChordLabel([1, 6, 10], 6, 10, 'Gb/3')

def test_explicit_chord():
    assert parse_chord('D:(b3,5,b7)') == ChordLabel([2, 0, 9, 5], 2, 2, 'D:(b3,5,b7)')

def test_basic_insane_chord():
    label = 'Cb#b#:maj7(4,#9,*5,bb7)/b9'
    assert parse_chord(label) == ChordLabel([0, 1, 3, 4, 5, 9, 11], 0, 1, label)

def test_sharp_chord():
    print(parse_chord('F#'))
    assert parse_chord('F#') == ChordLabel([1, 6, 10], 6, 6, 'F#')
