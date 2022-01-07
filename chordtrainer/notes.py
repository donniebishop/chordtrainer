#!/usr/bin/python3

import re

class Note:
    def __init__(self, name: str):
        if not re.findall('^[A-G][#|b]?', name):
            raise ValueError
        else:
            self.name = name

    def __repr__(self):
        return f"<Note: {self.name}>"

    def __str__(self):
        return self.name

    # this shit was magic and made everything work
    def __eq__(self, comp) -> bool:
        return self.name == comp

    def __hash__(self) -> int:
        return hash(self.name)

class Natural(Note):
    def __init__(self, name: str):
        super().__init__(name)

    def __repr__(self):
        return f"<Natural: {self.name}>"

class Accidental(Note):
    def __init__(self, name: str):
        super().__init__(name)

    # for when i actually move self.sharp and self.flat into this class
    # def __hash__(self) -> int:
    #     return hash((self.sharp, self.flat))

class Sharp(Accidental):
    def __init__(self, name: str):
        super().__init__(name)
        flats = {
            'A#': 'Bb',
            'C#': 'Db',
            'D#': 'Eb',
            'F#': 'Gb',
            'G#': 'Ab',
        }
        self.sharp = self.name
        self.flat = flats[self.name]

    def __repr__(self):
        return f"<Sharp: {self.name}>"

    def __eq__(self, comp) -> bool:
        return (self.sharp == comp) or (self.flat == comp)

    # overriding __eq__() sets __hash__() to return None
    def __hash__(self) -> int:
        return super().__hash__()

class Flat(Accidental):
    def __init__(self, name: str):
        super().__init__(name)
        sharps = {
            'Ab': 'G#',
            'Bb': 'A#',
            'Db': 'C#',
            'Eb': 'D#',
            'Gb': 'F#'
        }
        self.flat = self.name
        self.sharp = sharps[self.name]

    def __repr__(self):
        return f"<Flat: {self.name}>"

    def __eq__(self, comp) -> bool:
        return (self.sharp == comp) or (self.flat == comp)

    # overriding __eq__() sets __hash__() to return None
    def __hash__(self) -> int:
        return super().__hash__()

def bcef_accidentals(name: str) -> Natural:
    conversion = {
        'B#': Natural('C'),
        'Cb': Natural('B'),
        'E#': Natural('F'),
        'Fb': Natural('E'),
    }
    return conversion[name]

def make_note(name: str, type: str = None) -> Note:
    # sanitize input
    name = name.capitalize()
    if len(name) > 3:
        raise ValueError

    # build note
    if name in ['B#','Cb','E#','Fb']:
        return bcef_accidentals(name)
    if name.endswith('#') or (type == 'sharp'):
        return Sharp(name)
    elif name.endswith('b') or (type == 'flat'):
        return Flat(name)
    else:
        return Natural(name)

class Chromatic():
    def __init__(self) -> None:
        self.sharps = [make_note(n) for n in "A,A#,B,C,C#,D,D#,E,F,F#,G,G#".split(',')]
        self.flats = [make_note(n) for n in "Ab,A,Bb,B,C,Db,D,Eb,E,F,Gb,G".split(',')]
        self.notes = self.sharps

    # needed for indexing
    def __getitem__(self, key):
        return self.notes[key]

CHROMATIC = Chromatic()
NATURALS = [n for n in CHROMATIC.notes if type(n) == Natural]
SHARPS = [n for n in CHROMATIC.sharps if type(n) == Sharp]
FLATS = [n for n in CHROMATIC.flats if type(n) == Flat] 
