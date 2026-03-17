# Custom exception classes
class GardenError(Exception):
    """Base exception for garden-related problems."""
    pass

class PlantError(GardenError):
    """Exception for plant-specific problems."""
    pass

class WaterError(GardenError):
    """Exception for watering-related problems."""
    pass

class GardenManager:
    def __init__(self):
        self.plants = {}  # plant_name: {"water": level, "sun": hours}

    def add_plant(self, name, water_level, sunlight_hours):
        """Add a plant with validation."""
        if not name or not isinstance(name, str) or name.strip() == "":
            raise PlantError("Plant name cannot be empty or invalid")
        if not (1 <= water_level <= 10):
            raise WaterError(f"Water level {water_level} must be between 1 and 10")
        if not (2 <= sunlight_hours <= 12):
            raise ValueError(f"Sunlight hours {sunlight_hours} must be between 2 and 12")
        
        self.plants[name] = {"water": water_level, "sun": sunlight_hours}
        return f"Successfully added plant '{name}'"

    def water_plants(self, plant_names):
        """Water multiple plants with proper cleanup."""
        print("Opening garden watering system...")
        watered_plants = []
        try:
            for name in plant_names:
                if name not in self.plants:
                    raise PlantError(f"Plant '{name}' not found in garden")
                
                # Simulate watering by increasing water level
                self.plants[name]["water"] = min(10, self.plants[name]["water"] + 2)
                watered_plants.append(name)
                print(f"Watered plant '{name}' - water level now: {self.plants[name]['water']}")
        except PlantError as e:
            print(f"Error during watering: {e}")
        finally:
            print("Closing garden watering system...")
        
        return watered_plants

    def check_plant_health(self, name):
        """Check health of a specific plant."""
        if name not in self.plants:
            raise PlantError(f"Plant '{name}' not found in garden")
        
        plant = self.plants[name]
        if plant["water"] < 3:
            raise WaterError(f"Plant '{name}' has low water level ({plant['water']}) - needs watering")
        if plant["sun"] < 4:
            raise ValueError(f"Plant '{name}' has insufficient sunlight ({plant['sun']} hours) - needs more sun")
        
        return f"Plant '{name}' is healthy (water: {plant['water']}, sun: {plant['sun']} hours)"

def test_garden_management():
    print("=== Garden Management System Test ===")
    manager = GardenManager()
    
    print("\n1. Adding plants with valid inputs:")
    try:
        result = manager.add_plant("Rose", 5, 6)
        print(f"Success: {result}")
    except (PlantError, WaterError, ValueError) as e:
        print(f"Error: {e}")
    
    try:
        result = manager.add_plant("Tulip", 7, 8)
        print(f"Success: {result}")
    except (PlantError, WaterError, ValueError) as e:
        print(f"Error: {e}")
    
    print("\n2. Adding plants with invalid inputs:")
    try:
        manager.add_plant("", 5, 6)  # Invalid name
    except (PlantError, WaterError, ValueError) as e:
        print(f"Handled error: {e}")
    
    try:
        manager.add_plant("Daisy", 15, 6)  # Invalid water
    except (PlantError, WaterError, ValueError) as e:
        print(f"Handled error: {e}")
    
    try:
        manager.add_plant("Sunflower", 5, 20)  # Invalid sun
    except (PlantError, WaterError, ValueError) as e:
        print(f"Handled error: {e}")
    
    print("\n3. Watering plants (demonstrates finally block):")
    manager.water_plants(["Rose", "Tulip", "Nonexistent"])  # Mix of valid and invalid
    
    print("\n4. Checking plant health:")
    plants_to_check = ["Rose", "Tulip", "Daisy", "Sunflower"]
    for plant in plants_to_check:
        try:
            result = manager.check_plant_health(plant)
            print(f"Health check: {result}")
        except (PlantError, WaterError, ValueError) as e:
            print(f"Health check error for '{plant}': {e}")
    
    print("\n5. Demonstrating error recovery - system continues working:")
    try:
        result = manager.add_plant("Lily", 6, 7)
        print(f"Recovery success: {result}")
    except (PlantError, WaterError, ValueError) as e:
        print(f"Recovery error: {e}")
    
    print("\nGarden management system test completed!")
    print(f"Current garden status: {list(manager.plants.keys())} plants managed")

if __name__ == "__main__":
    test_garden_management()