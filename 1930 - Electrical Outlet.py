outlets_str = input().split()

outlets = [int(x) for x in outlets_str]

total_available_outlets = outlets[0]

for i in range(1, len(outlets)):
    total_available_outlets += (outlets[i] - 1)

print(total_available_outlets)
