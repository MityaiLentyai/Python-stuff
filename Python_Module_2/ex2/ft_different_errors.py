def garden_operations(operation_number: int) -> None:
    match operation_number:
        case 0:
            int("abc")
        case 1:
            15 / 0
        case 2:
            open("waat.txt", "r")
        case 3:
            "A" + 15


def test_error_types():

    print("=== Garden Error Types Demo ===")
    operation_list = [0, 1, 2, 3, 4]

    for op in operation_list:
        try:
            garden_operations(op)
        except ValueError as e:
            print(f"Testing operation {op}...")
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Testing operation {op} ...")
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Testing operation {op}...")
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Testing operation {op}...")
            print(f"Caught TypeError: {e}")
        else:
            print(f"Testing operation {op}...")
            print("Operation completed successfully")


test_error_types()
print()
print("All error types tested successfully!")
