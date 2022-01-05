#!/usr/bin/python3

class Note:
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self):
        return self.name

    # this shit was magic and made everything work
    def __eq__(self, comp):
        return self.name == comp

class Natural(Note):
    def __init__(self, name: str) -> Note:
        super().__init__(name)

class Accidental(Note):
    def __init__(self, name: str) -> Note:
        super().__init__(name)

        # TODO: Accidental construction fails if given a flat
        # sharps = {
        #     'Ab': 'G#',
        #     'Bb': 'A#',
        #     'Db': 'C#',
        #     'Eb': 'D#',
        #     'Gb': 'F#'
        # }
        # self.sharp = sharps[self.name]

        flats = {
            'A#': 'Bb',
            'C#': 'Db',
            'D#': 'Eb',
            'F#': 'Gb',
            'G#': 'Ab',
        }
        self.sharp = self.name
        self.flat = flats[self.name]

    def __eq__(self, comp):
        return (self.sharp == comp) or (self.flat == comp)

class Chromatic():
    def __init__(self) -> None:
        self.notes = [
            Natural('A'),
            Accidental('A#'),
            Natural('B'),
            Natural('C'),
            Accidental('C#'),
            Natural('D'),
            Accidental('D#'),
            Natural('E'),
            Natural('F'),
            Accidental('F#'),
            Natural('G'),
            Accidental('G#'),
        ]
        self.sharps = self.notes
        self.flats = [note.flat if type(note) == Accidental else note for note in self.notes]

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
    Accidental('A#'),
    Accidental('C#'),
    Accidental('D#'),
    Accidental('F#'),
    Accidental('G#')
]