#!/usr/bin/python3

from .notes import *

class Chord:
    def __init__(self, root: Note, type: str, formula: str):
        self.root = root
        self.type = type
        self.notes = self._set_notes(formula)
        self.inversion = None
        self.slash = False
        self.bass = None

    def __repr__(self):
        if self.slash:
            return "{r}/{b}".format(r=self.root, b=self.bass)
        elif self.inversion:
            return "{r}{t} {i} inversion".format(r=self.root, t=self.type, i=self.inversion)
        else:
            return "{r}{t}".format(r=self.root, t=self.type)

    # def __eq__(self, comp):
    #     for n in self.notes:
    #         if n not in comp.notes:
    #             return False
    #             break
    #         else:
    #             return True

    def _set_notes(self, formula: str) -> list:
        notes = [self.root]
        for num in formula.split(','):
            if int(num) == 1:
                continue
            note_index = CHROMATIC.notes.index(self.root) + (int(num))

            # account for chromatic list wraparound
            try:
                note = CHROMATIC.notes[note_index]
            except IndexError:
                note = CHROMATIC.notes[note_index - 12]
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
    def __init__(self, root: Note, type=' Major', formula="1,4,7"):
        super().__init__(root, type, formula)

class MinChord(Chord):
    def __init__(self, root: Note, type=' Minor', formula="1,3,7"):
        super().__init__(root, type, formula)

class DimChord(Chord):
    def __init__(self, root: Note, type=' Diminished', formula="1,3,6"):
        super().__init__(root, type, formula)

class Maj7Chord(Chord):
    def __init__(self, root: Note, type='maj7', formula="1,4,7,11"):
        super().__init__(root, type, formula)

class Min7Chord(Chord):
    def __init__(self, root: Note, type='m7', formula="1,3,7,10"):
        super().__init__(root, type, formula)

class Dom7Chord(Chord):
    def __init__(self, root: Note, type='7', formula="1,4,7,10"):
        super().__init__(root, type, formula)

class M7b5Chord(Chord):
    def __init__(self, root: Note, type='m7b5', formula="1,3,6,10"):
        super().__init__(root, type, formula)