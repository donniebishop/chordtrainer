#!/usr/bin/python3

from .notes import *
from .chord import *

class Scale:
    def __init__(self, root: Note, scale_type: str, formula: str):
        if type(root) is str:
            self.root = make_note(root)
        else:
            self.root = root

        if type(self.root) is Flat:
            self.prefer_flat = True
        else:
            self.prefer_flat = False
        
        self.scale_type = scale_type
        self.notes = self._set_notes(formula)
        self.chords = self._gen_chords()

    def __repr__(self):
        return "{r} {t}".format(r=self.root, t=self.scale_type)

    def __getitem__(self, key):
        return self.notes[key]

    def __eq__(self, comp):
        for n in self.notes:
            if n not in comp:
                return False
        return True
    
    def _set_notes(self, formula: str) -> list:
        current = self.root
        notes = [current]

        if self.prefer_flat:
            chromatic = CHROMATIC.flats
        else:
            chromatic = CHROMATIC.sharps

        for step in formula:
            if step == 'H':
                next_index = chromatic.index(current) + 1
            elif step == 'W':
                next_index = chromatic.index(current) + 2

            # account for chromatic list wraparound
            try:
                next = chromatic[next_index]
            except IndexError:
                next = chromatic[next_index - 12]

            notes.append(next)
            current = next
        return notes

    def _gen_chords(self) -> list:
        templates = {
            'major': 'MmmMMmd',
            'minor': 'mdMmmMM',
        }
        template = templates[self.scale_type.lower()]
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
    def __init__(self, root: Note, scale_type="Major", formula="WWHWWW"):
        super().__init__(root, scale_type, formula)

class MinorScale(Scale):
    def __init__(self, root: Note, scale_type="Minor", formula="WHWWHW"):
        super().__init__(root, scale_type, formula)

# doesn't work with W H
# class MinorPentatonicScale(Scale):
#     def __init__(self, root: Note, scale_type="Minor", formula="WHWWHW"):
#         super().__init__(root, scale_type, formula)
