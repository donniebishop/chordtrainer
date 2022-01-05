#!/usr/bin/python3 

def mode_select() -> int:
    print("Choose a Mode:")
    print("1: Scale Tones")
    print("2: Chord Tones")
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
        print("Sorry, mode {} is currently under construction.\n".format(mode))
        mode = mode_select()

main()