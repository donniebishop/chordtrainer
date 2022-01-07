#!/usr/bin/python3 

from chordtrainer.games import chord_trainer, scale_trainer

def mode_select() -> int:
    print("Choose a Mode:")
    print("1: Chord Tones")
    print("2: Scale Tones")
    print("0: Quit")

    mode = None
    while mode not in [1,2,0]:
        try:
            mode = int(input("\nMode: "))
        except ValueError:
            print("Please only choose numbers to choose a mode.")
            mode = None
    return mode

if __name__ == "__main__":
    mode = mode_select()
    while mode != 0:
        modes = {
            1: chord_trainer,
            2: scale_trainer
        }
        try:
            modes[mode]()
        except ValueError:
            print(f"Sorry, mode {mode} is currently under construction.\n")
        mode = mode_select()
