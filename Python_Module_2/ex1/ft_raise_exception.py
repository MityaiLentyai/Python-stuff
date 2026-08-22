def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    val = int(temp_str)
    if 0 <= val <= 40:
        print(f"Temperature now is {val}°C")
        return val
    elif val > 40:
        raise ValueError(f"{val}°C is too hot for plants (max 40°C)")
    else:
        raise ValueError(f"{val}°C is too cold for plants (min 0°C)")


def test_temperature() -> None:
    valid_input: str = "25"
    invalid_input: str = "abc"
    invalid_input_too_hot: str = "100"
    invalid_input_too_cold: str = "-50"

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

    try:
        input_temperature(invalid_input_too_hot)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    finally:
        print()

    try:
        input_temperature(invalid_input_too_cold)
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
