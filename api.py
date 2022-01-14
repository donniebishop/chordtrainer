#!/usr/bin/env python3

import uvicorn
from fastapi import FastAPI

from chordtrainer.notes import *
from chordtrainer.chord import *
from chordtrainer.scale import *

app = FastAPI()

@app.get('/')
def get_root():
    return "{'message': 'hello world'}"

@app.get('/chord/{chord_type}/{root}')
def get_chord(chord_type: str, root: str):
    chord_types = {
        'major':    MajChord,
        'minor':    MinChord,
        'dim':      DimChord,
        'maj7':     Maj7Chord,
        'min7':     Min7Chord,
        '7':        Dom7Chord,
        'm7b5':     M7b5Chord,
    }
    chord = chord_types[chord_type.lower()](root)
    return chord.__dict__

@app.get('/scale/{scale_type}/{root}')
def get_scale(scale_type:str, root: str):
    pass

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000, debug=True)