# Последовательность состоит из натуральных чисел и завершается числом 0. Определите значение наибольшего элемента
# последовательности.

max = -1
element = int(input())
while element != 0:
    if element > max:
        max = element
    element = int(input())
print(max)
