def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    test_input = "25"
    print(f"Input data is '{test_input}'")
    try:
        temp = input_temperature(test_input)
        print(f"Temperature is now {temp}\u00b0C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    test_input = "abc"
    print(f"Input data is '{test_input}'")
    try:
        temp = input_temperature(test_input)
        print(f"Temperature is now {temp}\u00b0C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
