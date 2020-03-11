#! /usr/bin/env python3
# -*- coding: utf-8 -*-

notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def decorator(func):
    def inner():
        print(" (灬╹ω╹灬) ")
        func()
        print("Bye~ Bye~")
    return inner

def find_scales(root):
    dist = notes.index(root)

    if dist > 0 :
        notes.extend(notes[:dist])

    ionian = [root, notes[dist+2], notes[dist+4], notes[dist+5], notes[dist+7], notes[dist+9], notes[dist+11]]
    dorian = [root, notes[dist+2], notes[dist+3], notes[dist+5], notes[dist+7], notes[dist+9], notes[dist+10]]
    phrygian = [root, notes[dist+1], notes[dist+3], notes[dist+5], notes[dist+7], notes[dist+8], notes[dist+10]]
    lydian = [root, notes[dist+2], notes[dist+4], notes[dist+6], notes[dist+7], notes[dist+9], notes[dist+11]]
    mixo_lydian = [root, notes[dist+2], notes[dist+4], notes[dist+5], notes[dist+7], notes[dist+9], notes[dist+10]]
    aeolian = [root, notes[dist+2], notes[dist+3], notes[dist+5], notes[dist+7], notes[dist+8], notes[dist+10]]
    locrian = [root, notes[dist+1], notes[dist+3], notes[dist+5], notes[dist+6], notes[dist+8], notes[dist+10]]
    harmonic_minor = [root, notes[dist+2], notes[dist+3], notes[dist+5], notes[dist+7], notes[dist+8], notes[dist+11]]


    print(
        f"  Ionian (Major)      {' '.join(ionian)}\n \
 Dorian              {' '.join(dorian)}\n \
 Phrygian            {' '.join(phrygian)}\n \
 Lydian              {' '.join(lydian)}\n \
 Mixo Lydian         {' '.join(mixo_lydian)}\n \
 Aeolian (Minor)     {' '.join(aeolian)}\n \
 Locrian             {' '.join(locrian)}\n \
 Harmonic Minor      {' '.join(harmonic_minor)}\n"
    )

@decorator
def main():
    while True:
        try:
            root = input("Enter root note:\n").upper()
            if root == "EXIT" or root == "QUIT" or root == "ESC" or root == "BYE" or root == "END":
                print("ヾ(~▽~)")
                break
            find_scales(root)
        except ValueError:
            print("°(°ˊДˋ°) ° try again...\n")

if __name__ == "__main__":
    main()