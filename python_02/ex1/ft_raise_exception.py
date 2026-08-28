def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise Exception(f"{temp}\u00b0C is too hot for plants (max 40\u00b0C)")
    if temp < 0:
        raise Exception(f"{temp}\u00b0C is too cold for plants (min 0\u00b0C)")
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")

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

    test_input = "100"
    print(f"Input data is '{test_input}'")
    try:
        temp = input_temperature(test_input)
        print(f"Temperature is now {temp}\u00b0C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    test_input = "-50"
    print(f"Input data is '{test_input}'")
    try:
        temp = input_temperature(test_input)
        print(f"Temperature is now {temp}\u00b0C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
