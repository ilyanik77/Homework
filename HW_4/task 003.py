# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

lst = list(map(int,input("Введите числа через пробел: ").split()))
lst_1 = []
for elem in lst:
    if elem not in lst_1:
        lst_1.append(elem)
print(lst)
print(lst_1)