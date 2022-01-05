#!/usr/bin/python3

from .notes import *
from .chord import *

class Scale:
    def __init__(self, root: Note, type: str, formula: str):
        self.root = root
        self.type = type
        self.notes = self._set_notes(formula)
        self.chords = self._gen_chords()

    def __repr__(self):
        return "{r} {t}".format(r=self.root, t=self.type)
    
    def _set_notes(self, formula: str) -> list:
        current = self.root
        notes = [current]
        for step in formula:
            if step == 'H':
                next_index = CHROMATIC.notes.index(current) + 1
            elif step == 'W':
                next_index = CHROMATIC.notes.index(current) + 2

            # use sharps or flats
            # if type(self.root) == Accidental:
            #     if self.root not in SHARPS:
            #         chrom = chromatic.flats
            # else:
            #     chrom = chromatic.sharps

            # account for chromatic list wraparound
            try:
                next = CHROMATIC[next_index]
            except IndexError:
                next = CHROMATIC[next_index - 12]

            notes.append(next)
            current = next
        return notes

    def _gen_chords(self) -> list:
        tones = {
            'major': 'MmmMMmd',
            'minor': 'mdMmmMM',
        }
        template = tones[self.type.lower()]
        chords = []
        zipper = zip(self.notes, template)
        for (root, chord) in zipper:
            if chord == 'M':
                c = MajChord(root)
            elif chord == 'm':
                c = MinChord(root)
            elif chord == 'd':
                c = DimChord(root)
            chords.append(c)
        return chords

class MajorScale(Scale):
    def __init__(self, root: Note, type="Major", formula="WWHWWW"):
        super().__init__(root, type, formula)

class MinorScale(Scale):
    def __init__(self, root: Note, type="Minor", formula="WHWWHW"):
        super().__init__(root, type, formula)

# doesn't work with W H
# class MinorPentatonicScale(Scale):
#     def __init__(self, root: Note, type="Minor", formula="WHWWHW"):
#         super().__init__(root, type, formula)
