import math


def game():
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    first_set: tuple = coordinate_input_1()
    distance_to_center = math.sqrt(
        (first_set[0] - 0.0) ** 2
        + (first_set[1] - 0.0) ** 2
        + (first_set[2] - 0.0) ** 2
    )
    print(f"Distance to center: {round(distance_to_center, 4)}\n")
    print("Get a second set of coordinates")
    second_set: tuple = coordinate_input_2()
    distance_between_the_two = math.sqrt(
        (first_set[0] - second_set[0]) ** 2
        + (first_set[1] - second_set[1]) ** 2
        + (first_set[2] - second_set[2]) ** 2
    )
    print(
        f"Distance  between the 2 sets of coordinates:"
        f" {round(distance_between_the_two, 4)}\n"
    )


def coordinate_input_1() -> tuple:
    while True:
        # fmt: off
        try:
            user_input = input(
                "Enter new coordinates Enter new"
                "coordinates as floats in format 'x,y,z': "
            ).split(',')
            x, y, z = tuple(float(value) for value in user_input)
            print(f"Got a first tuple: {x, y, z}")
            print("It includes: ", end="")
            print(f"X={x}, ", end="")
            print(f"Y={y}, ", end="")
            print(f"Z={z}")
            return x, y, z

        except Exception:
            print("Invalid syntax")
        # fmt: on


def coordinate_input_2() -> tuple:
    while True:
        # fmt: off
        try:
            user_input = input(
                "Enter new coordinates as floats in format 'x,y,z': "
            ).split(',')
            float_values = []
            for value in user_input:
                float_values.append(float(value))
            x, y, z = tuple(float_values)
            return x, y, z

        except Exception as e:
            print(f"Error on parameter '{value}': {e}")
        # fmt: on


game()
