# Последовательность состоит из натуральных чисел и завершается числом 0. Определите, сколько элементов этой
# последовательности равны ее наибольшему элементу.

maximum = 0
num_maximal = 0
element = -1
while element != 0:
    element = int(input())
    if element > maximum:
        maximum, num_maximal = element, 1
    elif element == maximum:
        num_maximal += 1
print(num_maximal)