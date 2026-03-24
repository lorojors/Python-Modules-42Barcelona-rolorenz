class Plant:
    """Base plant class with analytics capabilities."""

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        self._stats = self.Stats()

    class Stats:
        """Nested class for tracking plant statistics."""

        def __init__(self):
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def record_grow(self):
            self._grow_calls += 1

        def record_age(self):
            self._age_calls += 1

        def record_show(self):
            self._show_calls += 1

        def display(self):
            return (
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, "
                f"{self._show_calls} show"
            )

    @staticmethod
    def is_older_than_year(days):
        """Check if given days is more than a year."""
        return days > 365

    @classmethod
    def create_anonymous(cls):
        """Create an anonymous plant with default values."""
        return cls("Unknown plant", 0.0, 0)

    def grow(self):
        """Increase plant height."""
        self.height += 1.0
        self._stats.record_grow()

    def age_up(self):
        """Increase plant age."""
        self.age += 1
        self._stats.record_age()

    def show(self):
        """Display plant info and record statistics."""
        self._stats.record_show()
        return f"{self.name}: {self.height}cm, {self.age} days old"

    def get_stats(self):
        """Get statistics display string."""
        return self._stats.display()


class Flower(Plant):
    """Flower class with blooming capability."""

    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self._bloomed = False

    def bloom(self):
        """Make flower bloom."""
        self._bloomed = True

    def show(self):
        """Display flower info with bloom status."""
        base = super().show()
        bloom_status = (
            "is blooming beautifully!"
            if self._bloomed
            else "has not bloomed yet"
        )
        return f"{base}\nColor: {self.color}\n{self.name} {bloom_status}"


class Tree(Plant):
    """Tree class with shade production."""

    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._tree_stats = self.TreeStats()

    class TreeStats(Plant.Stats):
        """Extended stats for trees including shade calls."""

        def __init__(self):
            super().__init__()
            self._shade_calls = 0

        def record_shade(self):
            self._shade_calls += 1

        def display(self):
            base = super().display()
            return f"{base}\n{self._shade_calls} shade"

    def produce_shade(self):
        """Calculate and display shade area."""
        self._tree_stats.record_shade()
        length = self.height
        width = self.trunk_diameter
        return (
            f"Tree {self.name} now produces a shade of "
            f"{length}cm long and {width}cm wide."
        )

    def show(self):
        """Display tree info with trunk diameter."""
        base = super().show()
        return f"{base}\nTrunk diameter: {self.trunk_diameter}cm"

    def get_stats(self):
        """Get tree-specific statistics."""
        return self._tree_stats.display()


class Seed(Flower):
    """Seed class that holds number of seeds after blooming."""

    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self._seeds = 0

    def bloom(self):
        """Bloom and generate seeds."""
        super().bloom()
        self._seeds = 42

    def show(self):
        """Display seed info with seed count."""
        base = super().show()
        # Replace bloom status line to include seeds
        lines = base.split('\n')
        result = '\n'.join(lines[:-1])
        result += f"\nSeeds: {self._seeds}"
        if self._bloomed:
            result += f"\n{self.name} is blooming beautifully!"
        return result


def display_plant_stats(plant):
    """Display statistics for any kind of plant."""
    print(f"[statistics for {plant.name}]")
    print(plant.get_stats())


def main():
    """Main function demonstrating garden analytics."""
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(
        f"Is 30 days more than a year? -> "
        f"{Plant.is_older_than_year(30)}"
    )
    print(
        f"Is 400 days more than a year? -> "
        f"{Plant.is_older_than_year(400)}"
    )

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    print(rose.show())
    display_plant_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    print(rose.show())
    display_plant_stats(rose)

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    print(oak.show())
    display_plant_stats(oak)
    print("[asking the oak to produce shade]")
    print(oak.produce_shade())
    display_plant_stats(oak)

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    print(sunflower.show())
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age_up()
    sunflower.bloom()
    print(sunflower.show())
    display_plant_stats(sunflower)

    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    print(anonymous.show())
    display_plant_stats(anonymous)


if __name__ == "__main__":
    main()
