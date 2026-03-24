class Plant:
    """Plant class with immediate initialization."""

    def __init__(self, name, height, age):
        self.name = name
        self.height = float(height)
        self.age = age

    def show(self):
        """Display plant creation info."""
        return (
            f"Created: {self.name}: {self.height}cm, "
            f"{self.age} days old"
        )

    def grow(self):
        """Increase plant height."""
        self.height += 1.0


def main():
    """Create and display multiple plants."""
    print("=== Plant Factory Output ===")

    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    ]

    for plant in plants:
        print(plant.show())


if __name__ == "__main__":
    main()
