# Реализуйте алгоритм перемешивания списка
#  (метод random.shuffle использовать нельзя, но другие методы из библиотеки random - можно).

import random

list_1 = [1, 2, 3, 4, 5]
list_2 = random.sample(list_1, len(list_1))
print (f'Оригинальный список:  {list_1}')
print (f'Перемешанный список:  {list_2}')
