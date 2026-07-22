def ft_water_reminder():
    days_since_watering = int(input("Days since last watering: "))
    if days_since_watering > 2:
        print('water the plants!')
    else:
        print("plants are fine")
