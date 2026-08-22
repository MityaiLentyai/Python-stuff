def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    try:
        val = int(temp_str)
        print(f"Temperature now is '{val}'°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    finally:
        print()


def test_temperature():
    valid_input: int = 25
    invalid_input: str = "abc"

    input_temperature(valid_input)
    input_temperature(invalid_input)


def main() -> None:
    print("=== Garden Temperature ===")
    print()
    test_temperature()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
