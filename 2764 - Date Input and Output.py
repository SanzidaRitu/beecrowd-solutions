date_input = input()

day, month, year = map(str, date_input.split("/"))

print(f"{month}/{day}/{year}")

print(f"{year}/{month}/{day}")

print(f"{day}-{month}-{year}")