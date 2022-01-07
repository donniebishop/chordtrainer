import random
from .notes import *
from .chord import TRIADS, SEVENTH_CHORDS
from .scale import *

# Utils
# --------

def generate_random_note() -> Note:
    chromatic = random.choice([CHROMATIC.sharps, CHROMATIC.flats])
    note = random.choice(chromatic)
    return note

def generate_random_chord(root: Note = None, difficulty: int = 1) -> Chord:
    # setup type pool and choose chord
    difficulty_levels = [
        TRIADS,
        SEVENTH_CHORDS,
        #EXTENDED
    ]
    chord_types = []
    for level in range(difficulty):
        chord_types = [chord for chord in difficulty_levels[level]]
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

# Chord Trainer
# ----------------

def get_user_input_notes(choose: int) -> set:
    # use set to get dedup for "free"
    # requires __hash__() to be defined for any custom classes in the set
    user_notes = set()
    while len(user_notes) < choose:
        choice = input("Enter note: ")
        try:
            # wow i actually can't believe this works
            choices = choice.split(' ')
            for note in choices:
                if len(note) > 2:
                    raise IndexError
                user_notes.add(make_note(note))
        except IndexError:
            print("Please only enter one note at a time!")
    return user_notes 

def check_notes(guess: list, answer: Chord) -> bool:
    for note in guess:
        if note not in answer.notes:
            return False
    return True

def chord_trainer(lives: int = 3) -> None:
    level = 0
    while not (1 <= level <= 3):
        try:
            level = int(input("Choose Difficulty Level (1-3): "))
        except ValueError:
            pass

    score = 0
    answer = generate_random_chord(difficulty=level)
    print(f"What notes are in {answer}?")

    while lives:
        guesses = get_user_input_notes(choose=len(answer.notes))
        if check_notes(guesses, answer):
            print('Correct!\n')
            score += 1
            guesses = []
            answer = generate_random_chord(difficulty=level)
            print(f"What notes are in {answer}?")
        else:
            lives -= 1
            if lives == 0:
                correct_notes = [str(note) for note in answer.notes]
                print(f"Sorry, the correct answer is: {correct_notes}.\n")
                print(f"Your final score was: {score}")
            else:
                print(f"Wrong! Try again! {lives} lives remaining!\n")
    
# Scale Trainer
# ----------------

def get_user_input_chord() -> Chord:
    pass

def check_chord_in_scale(guess: Chord, answer: Scale) -> bool:
    return guess in list(answer.chords.values)

def scale_trainer(lives: int = 3) -> None:
    level = 0
    while not (1 <= level <= 5):
        try:
            level = int(input("Choose Difficulty Level (1-5): "))
        except ValueError:
            pass
    
    score = 0
    scale = generate_random_scale(difficulty=level)
    answer = random.choice(list(scale.chords.values()))
    print("QUESTION?")

    while lives:
        guess = get_user_input_chord()
        if check_chord_in_scale(guess, scale):
            score += 1
            guess = None
            scale = generate_random_scale(difficulty=level)
            print("QUESTION?")
        else:
            lives -= 1
            if lives <= 0:
                print(f"Your final score was: {score}")
            else:
                print(f"Wrong! Try again! {lives} lives remaining!\n")
