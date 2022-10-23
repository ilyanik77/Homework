# Наибольший общий делитель.
# В модуле math есть функция math.gcd(a, b), возвращающая наибольший общий делитель (НОД) двух чисел. 
# Вычислите и напечатайте наибольший общий делитель для списка натуральных чисел. 
# Ввод чисел продолжается до ввода пустой строки.

from functools import reduce
import math
lst = [36, 12, 144, 18]

def gcd(a, b):
    return gcd(b, a % b) if b else a

max_gsd = reduce(gcd, lst)
print(max_gsd)


