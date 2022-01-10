#!/usr/bin/python3

import re
from .notes import *

class Chord:
    def __init__(self, root: Note, chord_type: str, formula: list):
        if type(root) == str:
            self.root = make_note(root)
        else:
            self.root = root

        self.prefer_flat = type(self.root) is Flat
        self.notes = self._set_notes(formula)
        self.chord_type = chord_type
        self.inversion = None
        self.slash = False
        self.bass = None

    def __repr__(self) -> str:
        return f"<Chord root: {self.root}, chord_type: {self.chord_type.strip()}>"

    def __str__(self):
        if self.slash:
            return f"{self.root}/{self.bass}"
        elif self.inversion:
            return f"{self.root}{self.chord_type} {self.inversion} inversion"
        else:
            return f"{self.root}{self.chord_type}"

    def __eq__(self, other):
        return self._is_subset(other) and other._is_subset(self)

    def __hash__(self) -> int:
        return hash((self.root, self.chord_type))

    def __getitem__(self, key):
        return self.notes[key]

    def _is_subset(self, other):
        for n in self.notes:
            if n not in other:
                return False
        return True

    def _set_notes(self, formula: list) -> list:
        notes = [self.root]
        if self.prefer_flat:
            chromatic = CHROMATIC.flats
        else:
            chromatic = CHROMATIC.sharps

        for num in formula:
            if num == 0:
                continue
            note_index = chromatic.index(self.root) + num

            # account for chromatic list wraparound
            try:
                note = chromatic[note_index]
            except IndexError:
                note = chromatic[note_index - 12]
            notes.append(note)
        return notes

    def _set_inversion(self, inversion: int):
        self.inversion = 1
        for n in range(inversion):
            self.notes.append(self.notes.pop(0))

    def _set_slash(self, bass: Note) -> None:
        self.slash = True
        self.bass = bass

class MajChord(Chord):
    def __init__(self, root: Note, chord_type=' Major', formula=[0,4,7]):
        super().__init__(root, chord_type, formula)

class MinChord(Chord):
    def __init__(self, root: Note, chord_type=' Minor', formula=[0,3,7]):
        super().__init__(root, chord_type, formula)

class DimChord(Chord):
    def __init__(self, root: Note, chord_type=' Diminished', formula=[0,3,6]):
        super().__init__(root, chord_type, formula)

class Maj7Chord(Chord):
    def __init__(self, root: Note, chord_type='maj7', formula=[0,4,7,11]):
        super().__init__(root, chord_type, formula)

class Min7Chord(Chord):
    def __init__(self, root: Note, chord_type='m7', formula=[0,3,7,10]):
        super().__init__(root, chord_type, formula)

class Dom7Chord(Chord):
    def __init__(self, root: Note, chord_type='7', formula=[0,4,7,10]):
        super().__init__(root, chord_type, formula)

class M7b5Chord(Chord):
    def __init__(self, root: Note, chord_type='m7b5', formula=[0,3,6,10]):
        super().__init__(root, chord_type, formula)

class Dim7Chord(Chord):
    def __init__(self, root: Note, chord_type='dim7', formula=[0,3,6,9]):
        super().__init__(root, chord_type, formula)

class ExtendedChord(Chord):
    def __init__(self, root: Note, chord_type: str, extension_string: str):
        formulas = {
            'major': ('maj',[0,4,7,11]),
            'minor': ('m',[0,3,7,10]),
            'dominant': ('',[0,4,7,10])
        }
        chord_name, formula = formulas[chord_type]
        extensions = convert_extensions(extension_string)
        formula += extensions

        # holy shit i can't believe this works
        super().__init__(root, chord_name, formula)

def convert_extensions(extension_str: str) -> list[int]:
    semitones = []
    ext_to_semitones = {
        'b9': 1,
        '9': 2,
        '11': 5,
        '#11': 6,
        'b5': 6,
        '#5': 8,
        'b13': 8,
        '6': 9,
        '13': 9,
    }

    if extension_str == None:
        raise ValueError
    else:
        regex = re.findall(r"[#b]?1?\d", extension_str)
        for ext in regex:
            semitones.append(ext_to_semitones[ext])
    return semitones

TRIADS = [MajChord, MinChord, DimChord]
SEVENTH_CHORDS = [Maj7Chord, Min7Chord, Dom7Chord, Dim7Chord]
#EXTENDED = [MajExtChord], MinExtChord, DomExtChord]
