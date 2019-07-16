#Counting Sundays. How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#1 Jan 1900 was a Monday.
#April, June, September and November has 30 days. The rest have 31. February has 28, except on leap year.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def countingSundays():
    day = 2
    sunday_count = 0

    for year in range(1901,2001):

        for m in range(len(months)):

            day += months[m]
            if year % 4 == 0 and m == 1:
                day += 1
            if day % 7 == 0:
                sunday_count += 1

    print("Sundays:", sunday_count)

countingSundays()
