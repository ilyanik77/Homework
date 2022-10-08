# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
import math

n = int(input("Введите число: "))
list = []
for i in range(1, n + 1):
        list.append(f'{math.factorial(i)}')
print(list)





