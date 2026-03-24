def input_temperature(data):
    """
    Convert input data to integer and validate it's within plant-friendly.

    Args:
        data: Input data (expected to be string convertible to int)

    Returns:
        int: Valid temperature between 0 and 40 (inclusive)

    Raises:
        ValueError: If data cannot be converted to int or is out of range
    """
    temperature = int(data)

    if temperature > 40:
        raise ValueError(f"{temperature}°C is too hot for plants (max 40°C)")
    if temperature < 0:
        raise ValueError(f"{temperature}°C is too cold for plants (min 0°C)")

    return temperature


def test_temperature():
    """
    Test the input_temperature function with various inputs including edge.
    """
    test_cases = [
        ("25", True),
        ("abc", False),
        ("100", False),
        ("-50", False),
    ]

    print("=== Garden Temperature Checker ===")

    for data, should_succeed in test_cases:
        print(f"Input data is '{data}'")
        try:
            result = input_temperature(data)
            print(f"Temperature is now {result}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
