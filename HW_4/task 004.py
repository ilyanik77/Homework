# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.


from encodings import utf_8
from random import randint

def Polinome (k, file_name):
# формируем список коэффициентов многочлена 
    
    lst = []
    for i in range(k + 1):
        lst.append(randint(0, 100))
    print(lst)
# формируем уравнение
    res = ""
    for i in range(-k, 1):
        if i == 0:
           res += f"{lst[-i]}"
        elif k == 1:
            res += f"{lst[-i]}x + "
        else:
            res += f"{lst[-i]}x^{k} + "

    print(res)
# записываем в файл
    with open(file_name, "w", encoding = "utf_8") as f:
        f.write(res)
Polinome(4, "file.txt")
