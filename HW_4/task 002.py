# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

from re import I


n = int(input("Введите число n: "))
lst = []
i = 2
while n >= i:
    
    if n % i == 0:
        lst.append(i)
        n //= i
        
    else:
        i += 1
print(lst)