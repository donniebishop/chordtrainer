import random
from typing import List, Set, Tuple

from .notes import *
from .chord import TRIADS, SEVENTH_CHORDS, EXTENDED
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
        EXTENDED,
    ]
    chord_types = difficulty_levels[difficulty-1]
    chord = random.choice(chord_types) 
    
    # pick random note if not provided
    if not root:
        root = generate_random_note()

    # generate chord
    if difficulty == 3:
        base_chord = random.choice(['major','minor','dominant'])
        extension = generate_random_chord_extension()
        return chord(root, base_chord, extension)
    else:
        return chord(root)

def generate_random_chord_extension() -> str:
    extensions = ['b9','9','11','#11','b13','6','13']
    return random.choice(extensions)

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

def get_user_input_notes(choose: int = 3, _debug: bool = False, _notes: List[Note] = None) -> Set[Note]:
    # for testing, otherwise shouldn't be used
    if _notes != None and _debug:
        return _notes

    # use set to get dedup for "free"
    # requires __hash__() to be defined for any custom classes in the set
    user_notes = set()
    while len(user_notes) < choose:
        choice = input("Enter note: ")
        try:
            # wow i actually can't believe this works
            choices = choice.strip().split(' ')
            for note in choices:
                if len(note) > 2:
                    raise IndexError
                user_notes.add(make_note(note))
        except IndexError:
            print("Please only enter one note at a time!")
    return user_notes 

def check_notes(guess: List[Note], answer: Chord) -> bool:
    for note in guess:
        if note not in answer.notes:
            return False
    return True

def chord_trainer(lives: int = 3) -> None:
    level = 0
    while not (1 <= level <= 3):
        try:
            level = int(input("Choose difficulty level (1-3): "))
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
            if lives:
                print(f"Wrong! Try again! {lives} lives remaining!\n")
    else:
        correct_notes = [str(note) for note in answer.notes]
        print(f"\nSorry, the correct answer is: {correct_notes}")
        print(f"Your final score was: {score}")
    
# Scale Trainer
# ----------------

def get_user_input_chord(_debug: bool = False, _chord: Chord = None) -> Chord:
    # for testing, otherwise shouldn't be used
    if _debug and _chord != False:
        return _chord
    
    guess = input('Enter a chord: ')
    note, chord_type = guess.split(' ')  # only works for triads, need regex to match 7ths
    root = make_note(note)
    if chord_type.lower() == 'major':
        chord = MajChord(root)
    elif chord_type.lower() == 'minor':
        chord = MinChord(root)
    elif chord_type.lower() == 'diminished':
        chord = DimChord(root)
    return chord

def interval_to_roman(interval: int) -> str:
    roman = ['i','ii','iii','iv','v','vi','vii']
    return roman[interval - 1]

def check_chord_in_scale(guess: Chord, answer: Scale) -> bool:
    return guess in list(answer.chords.values())

def check_chord_is_correct(guess: Chord, answer: Chord) -> bool:
    return guess == answer

def generate_scale_trainer_answer(d_level: int) -> Tuple[Scale, Chord]:
    scale = generate_random_scale(difficulty=d_level)
    number = random.choice(list(scale.chords.keys()))
    chord = scale.chords[number]
    roman = interval_to_roman(number)
    if chord.chord_type == ' Major':
        roman = roman.upper()
    print(f"What is the {roman} chord in the {scale.root} {scale.scale_type} scale")
    return (scale, chord)

def scale_trainer(lives: int = 3) -> None:
    level = 0
    while not (1 <= level <= 5):
        try:
            level = int(input("Choose Difficulty Level (1-5): "))
        except ValueError:
            level = 1
    
    score = 0
    scale, answer = generate_scale_trainer_answer(level)

    while lives:
        guess = get_user_input_chord()
        in_scale = check_chord_in_scale(guess, scale)
        is_correct = check_chord_is_correct(guess, answer)
        if in_scale and is_correct:
            print('Correct!\n')
            score += 1
            guess = None
            scale, answer = generate_scale_trainer_answer(level)
        else:
            lives -= 1
            if lives:
                print(f"Wrong! Try again! {lives} lives remaining!\n")
    else:
        print(f"\nSorry, the correct answer is: {answer}")
        print(f"Your final score was: {score}")

# Chord Progression
# -------------------

# Game will generate chord progression "A-B-C" in a given scale and you have to identify the chord intervals like ii-V-I
# could even generate only common progressions like ii-V-I, I-IV-V-vi, vii-III-vi