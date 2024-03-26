def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False
year = 2024
year = int(year)
leap_year = is_year_leap(year)

print("год: ", year, leap_year)