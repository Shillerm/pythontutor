# Последовательность состоит из натуральных чисел и завершается числом 0. Определите, сколько элементов этой
# последовательности больше предыдущего элемента.

previous = 0
count = -1
current = int(input())
while current != 0:
    if current > previous:
        count += 1
    previous = current
    current = int(input())
print(count)