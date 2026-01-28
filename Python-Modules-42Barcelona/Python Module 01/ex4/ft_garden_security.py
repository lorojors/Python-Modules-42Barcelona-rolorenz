class SecurePlant:
    def __init__(self, name):
        self.__name = name
        self.__height = 0
        self.__age = 0
    
    def set_height(self, height):
        if height < 0:
            print(f"Security: Negative height rejected")
            return False
        self.__height = height
        return True
    
    def set_age(self, age):
        if age < 0:
            print(f"Security: Negative age rejected")
            return False
        self.__age = age
        return True
    
    def get_height(self):
        return self.__height
    
    def get_age(self):
        return self.__age
    
    def get_name(self):
        return self.__name
    
    def __str__(self):
        return f"{self.__name} ({self.__height}cm, {self.__age} days)"


if __name__ == "__main__":
    print("=== Garden Security System ===")
    
    plant = SecurePlant("Rose")
    print(f"Plant created: {plant.get_name()}")
    
    if plant.set_height(25):
        print(f"Height updated: {plant.get_height()}cm [OK]")
    
    if plant.set_age(30):
        print(f"Age updated: {plant.get_age()} days [OK]")
    
    print(f"Invalid operation attempted: height -5cm [REJECTED]")
    plant.set_height(-5)
    
    print(f"Current plant: {plant}")