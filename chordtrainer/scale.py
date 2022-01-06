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

    def __str__(self):
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
            next_index = chromatic.index(current) + int(step)
            try: # account for chromatic list wraparound
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
    def __init__(self, root: Note, scale_type="Major", formula="221222"):
        super().__init__(root, scale_type, formula)

class MinorScale(Scale):
    def __init__(self, root: Note, scale_type="Minor", formula="212212"):
        super().__init__(root, scale_type, formula)

# okay so now the scale formulas are fixed
# but I have no idea what I'm gonna do about chord scales
# _gen_chords() about to get real ugly
class MinorPentatonicScale(Scale):
    def __init__(self, root: Note, scale_type="Minor Pentatonic", formula="3223"):
        super().__init__(root, scale_type, formula)
