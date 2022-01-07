import random
import pytest
from chordtrainer.notes import *
from chordtrainer.scale import *
from chordtrainer.chord import *

# Notes
# ----------

def test_chromatic():
    assert CHROMATIC[6] == Note('D#')

def test_globals():
    assert NATURALS[4] == Natural('E')
    assert SHARPS[0] == Accidental('A#')
    assert FLATS[3] == Flat('Eb')
    assert MajChord in TRIADS
    assert Dim7Chord in SEVENTH_CHORDS

def test_enharmonic():
    assert Sharp('C#') == Flat('Db')

@pytest.mark.parametrize(
    "note, note_type", [
        ('Bb', Flat),
        ('B', Natural),
        ('B#', Natural), # calls helper bcef_accidentals()
        ('C#', Sharp),
        ('db', Flat) # lazy eval
    ])
def test_make_note(note, note_type):
    assert type(make_note(note)) is note_type

# Chords
# ----------

def test_chord_compare():
    f = Natural('F')
    a = Natural('A')
    chord1 = MajChord(f)
    chord2 = MinChord(a)
    chord3 = Maj7Chord(f)
    chord4 = MajChord(f)
    assert chord1 != chord2
    assert chord2 != chord3
    assert chord4 == chord1

@pytest.mark.parametrize(
    "notes, chord_type", [
        (['G','B','D'], MajChord),
        (['F','A','C','E'], Maj7Chord),
        (['F#','A#','C#','E#'], Maj7Chord),
        (['Bb','Db','F','Ab'], Min7Chord),
        (['D','F#','A','C'], Dom7Chord)
    ])
def test_chord_constructor(notes, chord_type):
    chord = chord_type(make_note(notes[0]))
    random.shuffle(notes)
    note_objs = [make_note(n) for n in notes]
    for n in note_objs:
        assert n in chord.notes

# Scale
# ----------

# this test is really cool cuz it proves I can check for modality
def test_scale_compare():
    scale_x = MinorScale(Natural('A'))
    scale_y = MajorScale(Natural('C'))
    assert scale_x == scale_y

def test_scale_constructor():
    notes = ['B','C#','D#','E','F#','G#','A#']
    random.shuffle(notes)
    note_objs = [make_note(n) for n in notes]
    scale = MajorScale(Natural('B'))

    for n in note_objs:
        assert n in scale.notes

def test_chord_scale_generator():
    chords = [
        MajChord('E'),
        MinChord('F#'),
        MinChord('G#'),
        MajChord('A'),
        MajChord('B'),
        MinChord('C#'),
        DimChord('D#')
    ]
    random.shuffle(chords)
    scale = MajorScale(Natural('E'))
    for c in chords:
        assert c in scale.chords.values()

# Misc
# ----------

def test_laziness_chord():
    foo = Min7Chord('A#')
    bar = Min7Chord(Sharp('A#'))
    assert foo == bar

def test_laziness_scale():
    foo = MajorScale('A#')
    bar = MajorScale(Sharp('A#'))
    assert foo == bar

def test_laziness_chord_in_scale():
    # because I had to implement __hash__, as an ancillary benefit
    # I can now use the actual chord number as the index (Bb is the IV of F)
    foo = MinorScale('F')
    bar = MinChord('Bb')
    assert bar == foo.chords[4]