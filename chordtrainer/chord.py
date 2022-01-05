#!/usr/bin/python3

from .notes import *

class Chord:
    def __init__(self, root: Note, chord_type: str, formula: str):
        if type(root) == str:
            self.root = make_note(root)
        else:
            self.root = root

        if type(self.root) == Flat:
            self.prefer_flat = True
        else:
            self.prefer_flat = False

        self.notes = self._set_notes(formula)
        self.chord_type = chord_type
        self.inversion = None
        self.slash = False
        self.bass = None

    def __repr__(self):
        if self.slash:
            return "{r}/{b}".format(r=self.root, b=self.bass)
        elif self.inversion:
            return "{r}{t} {i} inversion".format(r=self.root, t=self.chord_type, i=self.inversion)
        else:
            return "{r}{t}".format(r=self.root, t=self.chord_type)

    def __eq__(self, comp):
        for n in self.notes:
            if n not in comp:
                return False
        return True

    def __getitem__(self, key):
        return self.notes[key]

    def _set_notes(self, formula: str) -> list:
        notes = [self.root]
        if self.prefer_flat:
            chromatic = CHROMATIC.flats
        else:
            chromatic = CHROMATIC.sharps
        for num in formula.split(','):
            if int(num) == 1:
                continue
            note_index = chromatic.index(self.root) + (int(num))

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
    def __init__(self, root: Note, chord_type=' Major', formula="1,4,7"):
        super().__init__(root, chord_type, formula)

class MinChord(Chord):
    def __init__(self, root: Note, chord_type=' Minor', formula="1,3,7"):
        super().__init__(root, chord_type, formula)

class DimChord(Chord):
    def __init__(self, root: Note, chord_type=' Diminished', formula="1,3,6"):
        super().__init__(root, chord_type, formula)

class Maj7Chord(Chord):
    def __init__(self, root: Note, chord_type='maj7', formula="1,4,7,11"):
        super().__init__(root, chord_type, formula)

class Min7Chord(Chord):
    def __init__(self, root: Note, chord_type='m7', formula="1,3,7,10"):
        super().__init__(root, chord_type, formula)

class Dom7Chord(Chord):
    def __init__(self, root: Note, chord_type='7', formula="1,4,7,10"):
        super().__init__(root, chord_type, formula)

class M7b5Chord(Chord):
    def __init__(self, root: Note, chord_type='m7b5', formula="1,3,6,10"):
        super().__init__(root, chord_type, formula)

class Dim7Chord(Chord):
    def __init__(self, root: Note, chord_type='dim7', formula="1,3,6,9"):
        super().__init__(root, chord_type, formula)
