def ft_plant_age():
    age = int(input("Enter the age of the plant in days: "))
    if age < 60:
        harvest = "Plant needs more time to grow."
    else:
        harvest = "Plant is ready to harvest!"
    print(harvest)