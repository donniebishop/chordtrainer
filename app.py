#!/usr/bin/python3 

from chordtrainer.games import chord_trainer

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

def main():
    mode = mode_select()
    while mode != 0:
        if mode == 1:
            chord_trainer()
        else:
            print("Sorry, mode {} is currently under construction.\n".format(mode))
        mode = mode_select()

main()