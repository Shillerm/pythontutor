# Даны два целых числа A и В, A>B. Выведите все нечётные числа от A до B включительно, в порядке убывания. В этой
# задаче можно обойтись без инструкции if.

A = int(input())
B = int(input())
for i in range(A - (A + 1) % 2, B - B % 2, -2):
    print(i, end=' ')