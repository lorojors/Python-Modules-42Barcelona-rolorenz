class SecurePlant:
    """Secure plant class with data validation and encapsulation."""

    def __init__(self, name, height=0.0, age=0):
        self._name = name
        self._height = self._validate_height(height, True)
        self._age = self._validate_age(age, True)

    def _validate_height(self, height, is_init=False):
        """Validate height, return valid value or default."""
        if height < 0:
            msg = (
                f"{self._name}: Error, height can't be negative"
                if not is_init else
                "Error: height can't be negative"
            )
            print(msg)
            if is_init:
                print("Creating plant with default height")
            else:
                print("Height update rejected")
            return 0.0
        return float(height)

    def _validate_age(self, age, is_init=False):
        """Validate age, return valid value or default."""
        if age < 0:
            msg = (
                f"{self._name}: Error, age can't be negative"
                if not is_init else
                "Error: age can't be negative"
            )
            print(msg)
            if is_init:
                print("Creating plant with default age")
            else:
                print("Age update rejected")
            return 0
        return int(age)

    def set_height(self, height):
        """Set height with validation."""
        valid_height = self._validate_height(height)
        if valid_height == height or height >= 0:
            self._height = valid_height
            return True
        return False

    def set_age(self, age):
        """Set age with validation."""
        valid_age = self._validate_age(age)
        if valid_age == age or age >= 0:
            self._age = valid_age
            return True
        return False

    def get_height(self):
        """Get protected height."""
        return self._height

    def get_age(self):
        """Get protected age."""
        return self._age

    def get_name(self):
        """Get protected name."""
        return self._name

    def __str__(self):
        """String representation."""
        return (
            f"{self._name}: {self._height}cm, "
            f"{self._age} days old"
        )


def main():
    """Demonstrate secure plant system."""
    print("=== Garden Security System ===")

    plant = SecurePlant("Rose", 15.0, 10)
    print(f"Plant created: {plant}")

    if plant.set_height(25):
        print(f"Height updated: {plant.get_height():.0f}cm")

    if plant.set_age(30):
        print(f"Age updated: {plant.get_age()} days")

    plant.set_height(-5)

    plant.set_age(-10)

    print(f"Current state: {plant}")


if __name__ == "__main__":
    main()
