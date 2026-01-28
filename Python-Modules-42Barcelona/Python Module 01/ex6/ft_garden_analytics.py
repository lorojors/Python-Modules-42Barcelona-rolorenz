class GardenManager:
    gardens = []
    def __init__(self, name):
        self.name = name
        self.plants = []
        GardenManager.gardens.append(self)
    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.name}'s garden")
    def grow_plants(self):
        for plant in self.plants:
            plant.grow()
    def garden_report(self):
        print(f"=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant}")
        stats = GardenStats.calculate_stats(self.plants)
        print(f"Plants added: {len(self.plants)}, Total growth: {stats['total_growth']}cm")
        print(f"Plant types: {stats['regular']} regular, {stats['flowering']} flowering, {stats['prize']} prize flowers")
        print(f"Height validation test: {self.validate_heights()}")
        print(f"Garden scores - {self.name}: {self.calculate_score()}")
    def validate_heights(self):
        return all(plant.height >= 0 for plant in self.plants)
    def calculate_score(self):
        return sum(plant.score for plant in self.plants)
    @classmethod
    def create_garden_network(cls):
        return cls.gardens
class GardenStats:
    @staticmethod
    def calculate_stats(plants):
        total_growth = sum(plant.growth for plant in plants)
        regular = sum(1 for plant in plants if isinstance(plant, Plant))
        flowering = sum(1 for plant in plants if isinstance(plant, FloweringPlant))
        prize = sum(1 for plant in plants if isinstance(plant, PrizeFlower))
        return {
            'total_growth': total_growth,
            'regular': regular,
            'flowering': flowering,
            'prize': prize
        }
class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.growth = 0
    def grow(self):
        self.height += 1
        self.growth += 1
    def __str__(self):
        return f"{self.name}: {self.height}cm"
class FloweringPlant(Plant):
    def __init__(self, name, height, flower_color):
        super().__init__(name, height)
        self.flower_color = flower_color
    def __str__(self):
        return f"{self.name}: {self.height}cm, {self.flower_color} flowers (blooming)"
class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, flower_color, prize_points):
        super().__init__(name, height, flower_color)
        self.prize_points = prize_points
    def __str__(self):
        return f"{self.name}: {self.height}cm, {self.flower_color} flowers (blooming), Prize points: {self.prize_points}"
if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    alice_garden = GardenManager("Alice")
    alice_garden.add_plant(Plant("Oak Tree", 100))
    alice_garden.add_plant(FloweringPlant("Rose", 25, "red"))
    alice_garden.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

    alice_garden.grow_plants()
    alice_garden.garden_report()

    bob_garden = GardenManager("Bob")
    bob_garden.add_plant(Plant("Maple Tree", 90))
    bob_garden.garden_report()

    print(f"Total gardens managed: {len(GardenManager.create_garden_network())}")