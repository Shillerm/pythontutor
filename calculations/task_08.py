# Даны значения двух моментов времени, принадлежащих одним и тем же суткам: часы, минуты и секунды для каждого из
# моментов времени. Известно, что второй момент времени наступил не раньше первого. Определите, сколько секунд прошло
# между двумя моментами времени. Программа на вход получает три целых числа: часы, минуты, секунды, задающие первый
# момент времени и три целых числа, задающих второй момент времени. Выведите число секунд между этими моментами
# времени.

h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())

print(((h2 * 60 * 60) - (h1 * 60 * 60)) + ((m2 * 60) - (m1 * 60)) + (s2 - s1))