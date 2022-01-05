#!/usr/bin/python3

class Note:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
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

# def convert_accidental(note: Accidental) -> Accidental:
#     if type(note) is Sharp:
#         return 

class Chromatic():
    def __init__(self) -> None:
        self.notes = [
            Natural('A'),
            Sharp('A#'),
            Natural('B'),
            Natural('C'),
            Sharp('C#'),
            Natural('D'),
            Sharp('D#'),
            Natural('E'),
            Natural('F'),
            Sharp('F#'),
            Natural('G'),
            Sharp('G#'),
        ]
        self.sharps = self.notes
        self.flats = [Flat(note.flat) if type(note) is Sharp else note for note in self.notes]

    def __repr__(self):
        return self.notes

    # needed for indexing
    def __getitem__(self, key):
        return self.notes[key]

CHROMATIC = Chromatic()
NATURALS = [
    Natural('A'),
    Natural('B'),
    Natural('C'),
    Natural('D'),
    Natural('E'),
    Natural('F'),
    Natural('G')
]
SHARPS = [
    Sharp('A#'),
    Sharp('C#'),
    Sharp('D#'),
    Sharp('F#'),
    Sharp('G#')
]
FLATS = [
    Flat('Ab'),
    Flat('Bb'),
    Flat('Db'),
    Flat('Eb'),
    Flat('Gb'),
]