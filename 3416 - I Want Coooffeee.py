import math

students, total_litres, student_drinks_millilitres = map(int , input().split(" "))
total = students * student_drinks_millilitres
answer = math.ceil(total / (total_litres * 1000)) * total_litres
print(answer)