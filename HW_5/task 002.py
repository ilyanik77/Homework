# Создайте программу для игры с конфетами человек против человека.

import random

a = int(input("Введите количество конфет: "))
player = random.randint(1, 2)
print(f"Первый ход игрока №{player}")
while a > 0:
    if player == 1:
        
        player_1 = int(input("Игрок №1 возьмите не больше 28 конфет: "))
        a -= player_1
        print(f"Осталось {a} конфет")
        
        if a > 28:
                player_2 = int(input("Игрок №2 возьмите не больше 28 конфет: "))
                a -= player_2
                print(f"Осталось {a} конфет")
        elif a > 0 and a < 28:
            print("Выиграл player_2")
            break        
        else:
            print("Выиграл player_1")
            break
                
    else:
        player_2 = int(input("Игрок №2 возьмите не больше 28 конфет: "))
        a -= player_2
        print(f"Осталось {a} конфет")
        if a > 28:
            player_1 = int(input("Игрок №1 возьмите не больше 28 конфет: "))
            a -= player_1
            print(f"Осталось {a} конфет")
        elif a > 0 and a < 28:
            print("Выиграл player_1")
            break
        else:
            print("Выиграл player_2")
            break