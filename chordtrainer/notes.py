#!/usr/bin/python3

class Note:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    # this shit was magic and made everything work
    def __eq__(self, comp) -> bool:
        return self.name == comp

class Natural(Note):
    def __init__(self, name: str):
        super().__init__(name)

class Accidental(Note):
    def __init__(self, name: str):
        super().__init__(name)

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

    def __eq__(self, comp) -> bool:
        return (self.sharp == comp) or (self.flat == comp)

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

    def __eq__(self, comp) -> bool:
        return (self.sharp == comp) or (self.flat == comp)

def make_note(name: str, type: str = None) -> Note:
    if len(name) > 3:
        raise ValueError
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
NATURALS = [make_note(n, 'natural') for n in "ABCDEFG"]
SHARPS = [make_note(n,'sharp') for n in "A#,C#,D#,F#,G#".split(',')]
FLATS = [make_note(n,'flat') for n in "Ab,Bb,Db,Eb,Gb".split(',')]
