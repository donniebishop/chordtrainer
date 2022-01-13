import random

from chordtrainer.notes import *
from chordtrainer.games import *

def test_random_note_gen():
    note = generate_random_note()
    assert issubclass(note.__class__, (Note))

def test_random_chord_gen():
    chord = generate_random_chord(difficulty=random.choice([1,2,3]))
    assert issubclass(chord.__class__, (Chord))

def test_random_scale_gen():
    scale = generate_random_scale()
    assert issubclass(scale.__class__, Scale)

def test_check_notes():
    chord = generate_random_chord()
    notes = chord.notes
    random.shuffle(notes)
    assert check_notes(notes, chord)

def test_get_input_notes():
    note_list = [make_note(n) for n in ['F','A','C','E']]
    output = get_user_input_notes(_debug=True,_notes=note_list)
    assert note_list == output

def test_chord_trainer():
    pass