def count_harvest_recursive(day, days):
    if day > days:
        print("Harvest time!")
        return
    print(f"Day {day}")
    count_harvest_recursive(day + 1, days)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    count_harvest_recursive(1, days)
