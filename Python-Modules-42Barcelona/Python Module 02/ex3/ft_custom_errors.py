class GardenError(Exception):
    """A basic error for garden problems."""

    def __init__(self, message="Unknown garden error"):
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    """For problems with plants (inherits from GardenError)."""

    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    """For problems with watering (inherits from GardenError)."""

    def __init__(self, message="Unknown water error"):
        super().__init__(message)


def test_plant_error():
    """Raise a PlantError with a specific message."""
    raise PlantError("The tomato plant is wilting!")


def test_water_error():
    """Raise a WaterError with a specific message."""
    raise WaterError("Not enough water in the tank!")


def test_custom_errors():
    """
    Demonstrate custom error types and show that catching GardenError
    catches all garden-related errors.
    """
    print("=== Custom Garden Errors Demo ===")

    # Test PlantError
    print("Testing PlantError...")
    try:
        test_plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    # Test WaterError
    print("Testing WaterError...")
    try:
        test_water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    # Demonstrate that catching GardenError catches all garden-related errors
    print("Testing catching all garden errors...")

    try:
        test_plant_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        test_water_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
