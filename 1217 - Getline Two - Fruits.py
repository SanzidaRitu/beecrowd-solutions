n = int(input())

total_fruits = 0
total_cost = 0.0

for day in range(1, n + 1):
    cost = float(input())
    fruits = input().split()

    fruit_count = len(fruits)

    total_fruits += fruit_count
    total_cost += cost

    print(f"day {day}: {fruit_count} kg")

avg_fruits = total_fruits / n
avg_cost = total_cost / n

print(f"{avg_fruits:.2f} kg by day")
print(f"R$ {avg_cost:.2f} by day")