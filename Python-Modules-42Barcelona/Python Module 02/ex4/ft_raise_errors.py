def check_plant_health(plant_name, water_level, sunlight_hours):
    if not plant_name or not isinstance(plant_name, str) or plant_name.strip() == "":
        raise ValueError("Plant name cannot be empty or invalid")
    if not (1 <= water_level <= 10):
        raise ValueError(f"Water level {water_level} is out of range (must be between 1 and 10)")
    if not (2 <= sunlight_hours <= 12):
        raise ValueError(f"Sunlight hours {sunlight_hours} are out of range (must be between 2 and 12)")
    return f"Plant '{plant_name}' is healthy with water level {water_level} and {sunlight_hours} hours of sunlight!"

def test_plant_checks():
    print("=== Plant Health Check Tests ===")
    
    test_cases = [
        ("Good values", "Rose", 5, 6),
        ("Bad plant name (empty)", "", 5, 6),
        ("Bad water level (too high)", "Rose", 15, 6),
        ("Bad water level (too low)", "Rose", 0, 6),
        ("Bad sunlight hours (too high)", "Rose", 5, 20),
        ("Bad sunlight hours (too low)", "Rose", 5, 1),
        ("Invalid plant name (non-string)", 123, 5, 6)
    ]
    
    for description, plant, water, sun in test_cases:
        print(f"\nTesting: {description}")
        try:
            result = check_plant_health(plant, water, sun)
            print(f"Success: {result}")
        except ValueError as e:
            print(f"Error: {e}")
        print("Test completed - program continues!")

if __name__ == "__main__":
    test_plant_checks()