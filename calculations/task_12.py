# Дано два числа a и b. Выведите гипотенузу треугольника с заданными катетами.

import math
a = float(input())
b = float(input())

print(math.sqrt((a * a) + (b * b)))