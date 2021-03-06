# Последовательность Фибоначчи определяется так: φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.
# По данному числу n определите n-е число Фибоначчи φn. Эту задачу можно решать и циклом for.

n = int(input())
if n == 0:
    print(0)
else:
    previous_1, previous_2 = 0, 1
    for i in range(2, n + 1):
        previous_1, previous_2 = previous_2, previous_1 + previous_2
print(previous_2)