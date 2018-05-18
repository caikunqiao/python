numbers = list(range(1,10))
ordinals = []

for number in numbers:
    if number == 1:
        ordinal = str(number) + "st"
        ordinals.append(ordinal)
    elif number == 2:
        ordinal = str(number) + "nd"
        ordinals.append(ordinal)
    elif number == 3:
        ordinal = str(number) + "rd"
        ordinals.append(ordinal)
    else:
        ordinal = str(number) + "th"
        ordinals.append(ordinal)

for ordinal in ordinals:
    print(ordinal)