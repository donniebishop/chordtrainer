#!/usr/bin/python3

from typing import List, Dict
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

    def __repr__(self) -> str:
        return f"<Scale root: {self.root}, scale_type: {self.scale_type}"

    def __str__(self):
        return f"{self.root} {self.scale_type}"

    def __getitem__(self, key) -> Note:
        return self.notes[key]

    def __eq__(self, comp):
        for n in self.notes:
            if n not in comp:
                return False
        return True
    
    def _set_notes(self, formula: str) -> List[int]:
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

    def _gen_chords(self) -> Dict[int, Chord]:
        templates = {
            'major': 'MmmMMmd',
            'minor': 'mdMmmMM',
        }
        template = templates[self.scale_type.lower()]
        chords = dict()
        zipper = zip(self.notes, template, range(len(template)))
        for (root, chord, index) in zipper:
            index += 1
            if chord == 'M':
                chords[index] = MajChord(root)
            elif chord == 'm':
                chords[index] = MinChord(root)
            elif chord == 'd':
                chords[index] = DimChord(root)
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
