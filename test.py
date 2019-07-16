day = 0
mon = 0
while mon != 12:
    if mon == 3 or mon == 5 or mon == 8 or mon == 10:
        day = day % 30
        if day == 29:
            mon += 1

    elif mon == 1:
        day = day % 28
        if day == 27:
            mon += 1

    else:
        day = day % 31
        if day == 30:
            mon += 1

    day += 1
    print(mon + 1, day + 1)
