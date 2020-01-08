# Дано положительное действительное число X. Выведите его первую цифру после десятичной точки.

from math import floor

x = float(input())
y = 10 * (x - int(x))
f = floor(y)
print(f)