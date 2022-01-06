import random
from .notes import *
from .chord import TRIADS, SEVENTH_CHORDS
from .scale import *

def generate_random_note() -> Note:
    chromatic = random.choice([CHROMATIC.sharps, CHROMATIC.flats])
    note = random.choice(chromatic)
    return note

def generate_random_chord(root: Note = None, include_sevenths: bool = False) -> Chord:
    # setup type pool and choose chord
    chord_types =  TRIADS
    if include_sevenths:
        chord_types += SEVENTH_CHORDS
    chord = random.choice(chord_types) 
    
    # pick random note if not provided
    if not root:
        root = generate_random_note()

    # generate chord
    return chord(root)

def generate_random_scale(root: Note = None, difficulty: int = 1) -> Scale:
    # setup type pool and choose scale
    difficulty_levels = [
        [MajorScale, MinorScale],
        # [MajPentatonic, MinPentatonic],
        # [HarmMinor, MelMinor],
        # [Dorian, Phrygian, Lydian, Mixolydian, Locrian],
        # [WholeTone, Diminished, Altered]
    ]
    scale_types = []
    for level in range(difficulty):
        scale_types += difficulty_levels[level]
    scale = random.choice(scale_types)

    # pick random note if not provided
    if not root:
        root = generate_random_note()
    
    # generate scale
    return scale(root)

def get_user_input_notes(choose: int) -> list:
    user_notes = []
    while len(user_notes) < choose:
        choice = input("Enter note: ")
        if len(choice) > 2:
            print("Please only enter one note at a time!")
            continue
        user_notes.append(make_note(choice))
    return user_notes 

def chord_trainer(retry: int = 3) -> None:
    chances = retry
    target_chord = generate_random_chord()
    correct_notes = target_chord.notes
    print(f"What notes are in {target_chord}?")

    while chances:
        user_notes = get_user_input_notes(choose=len(correct_notes))
        if user_notes == target_chord.notes:
            print('Correct!')
            break
        else:
            print('Wrong! Try again!\n')
            chances -= 1
    
    if chances == 0:
        correct_note_names = [note.name for note in correct_notes]
        print(f"Sorry, the correct answer is {correct_note_names}.")

def scale_trainer() -> None:
    pass