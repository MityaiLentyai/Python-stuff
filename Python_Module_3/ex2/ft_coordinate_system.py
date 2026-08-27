import math


def game():
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")

    # fmt: off
    try:
        coords = int(input(
            "Enter new coordinates Enter new"
            "coordinates as floats in format 'x,y,z': "
        ))
    except Exception:
        print("Invalid syntax")
    
    # fmt: on


game()
