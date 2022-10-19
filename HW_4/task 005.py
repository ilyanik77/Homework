# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов


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
            k -= 1
    print(res)
# записываем в файл
    with open(file_name, "w", encoding = "utf_8") as f:
        f.write(res)

Polinome(3, "file_1.txt")
Polinome(2, "file_2.txt")

#with open("file_1.txt") as f1, open("file_2.txt") as f2:
