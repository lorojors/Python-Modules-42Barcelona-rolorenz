def ft_water_reminder():
    days = int(input("How many days since last watering? "))
    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")