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
        try:
            # wow i actually can't believe this works
            choices = choice.split(' ')
            for note in choices:
                if len(note) > 2:
                    raise IndexError
                user_notes.append(make_note(note))
        except IndexError:
            print("Please only enter one note at a time!")
    return user_notes 

def check_answer(guess: list, answer: list) -> bool:
    for note in guess:
        if note not in answer:
            return False
    return True

def chord_trainer(lives: int = 3) -> None:
    target = generate_random_chord()
    answer = target.notes
    print(f"What notes are in {target}?")

    while lives:
        guesses = get_user_input_notes(choose=len(answer))
        if check_answer(guesses, answer):
            print('Correct!\n')
            guesses = []
            target = generate_random_chord()
            answer = target.notes
            print(f"What notes are in {target}?")
        else:
            lives -= 1
            if lives == 0:
                correct_notes = [note.name for note in answer]
                print(f"Sorry, the correct answer is {correct_notes}.\n")
            else:
                print(f"Wrong! Try again! {lives} lives remaining!\n")
    

def scale_trainer() -> None:
    pass