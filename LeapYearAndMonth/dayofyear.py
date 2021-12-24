def is_year_leap(year):
#
# Your code from LAB 4.3.1.6.
#
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

def days_in_month(year, month):
#
# Your code from LAB 4.3.1.7.
#
    if month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 30

def day_of_year(year, month, day):
#
# Write your new code here.
#
    day_of_year = 0
    if month in range(1, 13):
        for i in range(1, month):
            day_of_year += days_in_month(year, i)
    else:
        return None
    if day in range(1, 32):
        if day <= days_in_month(year, month):
            return day_of_year + day
        else:
            return None
    else:
        return None

print(day_of_year(2000, 12, 31))
print(day_of_year(2000, 2, 29))
print(day_of_year(2000, 11, 31))
print(day_of_year(1900, 2, 29))
print(day_of_year(1900, 2, 28))
print(day_of_year(1920, 5, 32))
print(day_of_year(1900, 35, 31))
print(day_of_year(2021, 12, 31))
print(day_of_year(2020, 12, 31))
