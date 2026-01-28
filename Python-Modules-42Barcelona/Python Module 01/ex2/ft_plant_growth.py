class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def grow(self):
        self.height += 1
    def age(self):
        self.age += 1
    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"
def main():
    rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    print(rose.get_info())
    initial_height = rose.height
    for day in range(6):
        rose.grow()
        rose.age()
        print("=== Day 7 ===")
    print(rose.get_info())
    growth = rose.height - initial_height
    print(f"Growth this week: +{growth}cm")
if __name__ == "__main__":
    main()