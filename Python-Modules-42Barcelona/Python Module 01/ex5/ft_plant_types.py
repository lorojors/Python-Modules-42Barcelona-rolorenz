class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    
    def __str__(self):
        return f"{self.name}: {self.height}cm, {self.age} days"


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
    
    def bloom(self):
        return f"{self.name} is blooming beautifully!"
    
    def __str__(self):
        return f"{super().__str__()}, {self.color} color"


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
    
    def produce_shade(self):
        shade_area = (self.trunk_diameter ** 2) * 0.1
        return f"{self.name} provides {shade_area:.0f} square meters of shade"
    
    def __str__(self):
        return f"{super().__str__()}, {self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
    
    def __str__(self):
        return f"{super().__str__()}, {self.harvest_season} harvest"


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    
    # Flowers
    rose = Flower("Rose", 25, 30, "red")
    print(f"Rose (Flower): {rose}")
    print(rose.bloom())
    
    tulip = Flower("Tulip", 30, 20, "yellow")
    print(f"Tulip (Flower): {tulip}")
    print(tulip.bloom())
    
    # Trees
    oak = Tree("Oak", 500, 1825, 50)
    print(f"Oak (Tree): {oak}")
    print(oak.produce_shade())
    
    pine = Tree("Pine", 400, 1460, 40)
    print(f"Pine (Tree): {pine}")
    print(pine.produce_shade())
    
    # Vegetables
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    print(f"Tomato (Vegetable): {tomato}")
    print(f"Tomato is rich in {tomato.nutritional_value}")
    
    carrot = Vegetable("Carrot", 30, 120, "fall", "vitamin A")
    print(f"Carrot (Vegetable): {carrot}")
    print(f"Carrot is rich in {carrot.nutritional_value}")