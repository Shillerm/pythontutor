# Даны два целых числа A и В, A>B. Выведите все нечётные числа от A до B включительно, в порядке убывания. В этой
# задаче можно обойтись без инструкции if.

A = int(input())
B = int(input())

if A % 2 != 0:
    for number in range(A, B - 1, - 2):
        print(number)
elif A % 2 == 0:
    for number in range(A - 1, B - 1, - 2):
        print(number)
