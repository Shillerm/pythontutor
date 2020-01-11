# Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно.

A = int(input())
B = int(input())

for number in range(A, B + 1):
    print(number)
