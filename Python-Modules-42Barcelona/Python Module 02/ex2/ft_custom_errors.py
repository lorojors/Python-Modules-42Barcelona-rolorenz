class GardenError(Exception):
    """Base exception for garden-related problems."""
    pass

class PlantError(GardenError):
    """Exception for plant-specific problems."""
    pass

class WaterError(GardenError):
    """Exception for watering-related problems."""
    pass

def garden_task(task_type):
    if task_type == "plant_bad":
        raise PlantError("Plant is not growing properly - check soil conditions")
    elif task_type == "water_low":
        raise WaterError("Water level is too low - irrigation system needs maintenance")
    elif task_type == "general":
        raise GardenError("General garden issue - please inspect the garden")

def test_custom_errors():
    print("Testing custom garden error types:")
    
    tasks = [
        ("plant_bad", "PlantError"),
        ("water_low", "WaterError"),
        ("general", "GardenError")
    ]
    
    for task, expected in tasks:
        print(f"\nTesting {task}:")
        try:
            garden_task(task)
        except PlantError as e:
            print(f"Caught PlantError: {e}")
        except WaterError as e:
            print(f"Caught WaterError: {e}")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
        print("Program continues after handling the error!")
    
    print("\nDemonstrating that catching GardenError catches all garden-related errors:")
    for task, _ in tasks:
        print(f"\nTesting {task} with broad GardenError catch:")
        try:
            garden_task(task)
        except GardenError as e:
            print(f"Caught with GardenError: {type(e).__name__}: {e}")
            print("This shows inheritance - PlantError and WaterError are caught by GardenError")
        print("Program continues!")

if __name__ == "__main__":
    test_custom_errors()