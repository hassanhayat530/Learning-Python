year_1 = int(input())
year_2 = int(input())
year_2 += 1
list_years = []
total_days = 0
for year in range(year_2-year_1):
    list_years.append(year_1)
    year_1 += 1
for year in list_years:
    if year % 400 == 0:
        total_days += 366
    else:
        if year % 100 == 0:
            total_days += 365
        else:
            if year % 4 == 0:
                total_days += 366
            else:
                total_days += 365
print(total_days)