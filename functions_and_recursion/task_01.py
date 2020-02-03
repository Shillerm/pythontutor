# Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние
# между точкой (x1,y1) и (x2,y2). Считайте четыре действительных числа и выведите результат работы этой функции.

from math import sqrt


def distance(x1, y1, x2, y2):
    c = sqrt(((x1 - x2) ** 2 + (y1 - y2) ** 2))
    print(format(c, '.4f'))


distance(float(input()), float(input()), float(input()), float(input()))
