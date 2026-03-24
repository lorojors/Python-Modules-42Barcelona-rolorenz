class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def __str__(self):
        return f"{self.name} : Height: {self.height}cm, Age: {self.age} days"


plant1 = Plant("Tomato", 45, 60)
plant2 = Plant("Basil", 30, 25)
plant3 = Plant("Sunflower", 120, 90)

plants = [plant1, plant2, plant3]

print("=== Garden Plant Registry ===")
for i in range(len(plants)):
    print(plants[i])
