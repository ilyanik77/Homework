# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

lst = [int(i) for i in (input("Введите числа: "))]
lst_1 = []
i = 0
while i < len(lst)/2:
    lst_1.append(lst[i] * lst[-1 - i])
    i += 1
print(lst)
print(lst_1)
