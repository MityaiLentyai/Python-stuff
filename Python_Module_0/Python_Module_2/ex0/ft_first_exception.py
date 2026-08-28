def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    val = int(temp_str)
    print(f"Temperature now is {val}°C")
    return val


def test_temperature() -> None:
    valid_input: str = "25"
    invalid_input: str = "abc"

    try:
        input_temperature(valid_input)
    except ValueError as e:
        print(f"Should never print: {e}")
    finally:
        print()

    try:
        input_temperature(invalid_input)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    finally:
        print()


def main() -> None:
    print("=== Garden Temperature ===")
    print()
    test_temperature()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
