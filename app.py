#!/usr/bin/python3 

from chordtrainer.games import chord_trainer, scale_trainer

def mode_select() -> int:
    print("\nChoose a Mode:")
    print("--------------")
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
            # when you're in a mode, if you submit an empty string during input()
            # this incidentally will catch the ValueError and act as a sort of quit-out.
            # it's not a bug. it's a feature.
            print(f"Sorry, mode {mode} is currently under construction.\n")
        mode = mode_select()
