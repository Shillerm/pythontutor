# Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.

list_one = input().split()
for i in range(len(list_one)):
    if int(list_one[i]) > int(list_one[i - 1]) and [i - 1] != [-1]:
        print(list_one[i], end=' ')
