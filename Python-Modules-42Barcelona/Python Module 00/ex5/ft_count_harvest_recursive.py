def ft_count_harvest_recursive(day=1):
    days_until_harvest = int(input("Days until harvest: "))
    if day <= days_until_harvest:
        print(f"Day {day}")
        ft_count_harvest_recursive(day + 1)
    else:
        print("Harvest time!")