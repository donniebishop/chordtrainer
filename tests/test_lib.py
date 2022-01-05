import random
import pytest
from chordtrainer.notes import *
from chordtrainer.scale import *
from chordtrainer.chord import *

def test_chromatic():
    assert CHROMATIC[6] == Note('D#')

def test_globals():
    assert NATURALS[4] == Natural('E')
    assert SHARPS[0] == Accidental('A#')
    assert FLATS[3] == Flat('Eb')

def test_enharmonic():
    assert Sharp('C#') == Flat('Db')

def test_chord_compare():
    chord1 = MajChord('D')
    chord2 = MinChord('D')
    chord3 = MajChord('D')

    assert chord1 != chord2
    assert chord1 == chord3

@pytest.mark.parametrize(
    "notes,chord_type", [
        (['G','B','D'], MajChord),
        (['F','A','C','E'], Maj7Chord),
        # (['F#','A#','C#','E#'], Maj7Chord),   # doesn't know how to deal with E#/Fb or other enharmonics
        (['Bb','Db','F','Ab'], Min7Chord),
        (['D','F#','A','C'], Dom7Chord)
    ])
def test_chord_constructor(notes, chord_type):
    chord = chord_type(Note(notes[0]))
    random.shuffle(notes)
    note_objs = [Note(n) for n in notes]
    for n in note_objs:
        assert n in chord.notes

def test_scale_constructor():
    notes = ['B','C#','D#','E','F#','G#','A#']
    random.shuffle(notes)
    note_objs = [Note(n) for n in notes]
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
        assert c in scale.chords
