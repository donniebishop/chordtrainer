import random
from chordtrainer.notes import *
from chordtrainer.scale import *
from chordtrainer.chord import *

def test_chromatic():
    assert CHROMATIC[6] == Accidental('D#')

def test_naturals():
    assert NATURALS[4] == Natural('E')

def test_sharps():
    assert SHARPS[0] == Accidental('A#')

def test_chord_constructor():
    notes = ['G','B','D','F#']
    random.shuffle(notes)
    note_objs = [Note(note) for note in notes]
    chord = Maj7Chord(Natural('G'))

    for n in note_objs:
        assert n in chord.notes

def test_scale_constructor():
    notes = ['B','C#','D#','E','F#','G#','A#']
    random.shuffle(notes)
    note_objs = [Note(note) for note in notes]
    scale = MajorScale(Natural('B'))

    for n in note_objs:
        assert n in scale.notes