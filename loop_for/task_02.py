# Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания, если A < B,
# или в порядке убывания в противном случае.

A = int(input())
B = int(input())

step = 1 if A < B else -1
for number in range(A, B + step, step):
    print(number)