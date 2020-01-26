# Определите среднее значение всех элементов последовательности, завершающейся числом 0.

n = 0
sum = 0
element = int(input())
while element != 0:
    sum += element
    n += 1
    element = int(input())
print(sum/n)