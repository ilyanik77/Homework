# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.

sum = 0
number = input('Введите число: ')

for a in number:
    if a.isdigit():
        sum += int(a)

print(sum)      