# Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.

list_one = [int(i) for i in input().split()]
counter = 1
for i in range(len(list_one) - 1):
    if list_one[i] != list_one[i + 1]:
        counter += 1
print(counter)
