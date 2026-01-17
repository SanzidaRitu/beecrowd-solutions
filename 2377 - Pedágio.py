L, D = map(int, input().split())
K, P = map(int, input().split())

travel_cost = L * K

num_tolls = L // D

toll_cost = num_tolls * P

total_cost = travel_cost + toll_cost

print(total_cost)