def day_converter(num):
    if num == 1:
        day = "Monday"
    elif num == 2:
        day = "Tuesday"
    elif num == 3:
        day = "Wednesday"
    elif num == 4:
        day = "Thursday"
    elif num == 5:
        day = "Friday"
    elif num == 6:
        day = "Saturday"
    else:
        day = "Sunday"
    return day

print(day_converter(1))
print(day_converter(2))
print(day_converter(3))
print(day_converter(4))
print(day_converter(5))
print(day_converter(6))
print(day_converter(7))