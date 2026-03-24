def water_plants(plant_list):
    print("Opening watering system...")
    try:
        for plant in plant_list:
            if not isinstance(plant, str) or plant.strip() == "":
                raise ValueError(f"Invalid plant name: '{plant}'")
            print(f"Watering {plant}...[OK]")
    except ValueError as e:
        print(f"Error during watering: {e}")
    finally:
        print("Closing watering system...")


def test_watering_system():
    print("=== Garden Watering System Test ===")

    print("\n1. Testing normal watering with valid plant list:")
    water_plants(["Rose", "Tulip", "Daisy"])

    print("\n2. Testing watering with invalid plant name (empty string):")
    water_plants(["Rose", "", "Daisy"])

    print("\n3. Testing watering with non-string plant name:")
    water_plants(["Rose", 123, "Daisy"])

    print("\nAll tests completed")


if __name__ == "__main__":
    test_watering_system()
