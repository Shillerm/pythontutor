# Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел. Подсчитайте количество нулей среди
# введенных чисел и выведите это количество. Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр.

number_zero = 0
for i in range(int(input())):
    if int(input()) == 0:
        number_zero += 1
print(number_zero)