# Задайте список из N элементов, заполненных числами из промежутка [-N, N]
# (например, [-3, -2, 1, 0, 1, 2, 3]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import Random, randint

N = int(input("Введите число: "))
numbers = []
for i in range(-N, N + 1):
    numbers.append(i)
print(list(numbers))

f = open('file.txt', 'w')

a = input("Позиция 1: ")
b = input("Позиция 2: ")
    
f.write('a \n')
f.write('b \n')
f.close()

f = open('file.txt', 'r')
result = 1
for line in f:
    if line == "":
        break
    result = numbers[int(a)] * numbers[int(b)]
f.close()
print(result)