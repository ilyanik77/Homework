# Вычислить число c заданной точностью d

from math import pi

d = int(input("Введите число d: "))
def RoundPi (pi, d):
    
    res = round(pi, d)
    return res

print(RoundPi(pi, d))