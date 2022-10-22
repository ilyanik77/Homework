# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


with open('file.txt', 'w') as data:
    data.write('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')

with open('file.txt', 'r') as data:
    string = data.readline()

def Encrypt(string):
    res = ''
    count = 0
    a = string[0]
    for i in range(0, len(string)):
        if string[i] == a:
            count += 1
            
        else:
            res = res + str(count) + a
            a = string[i]
            count = 1
    res = res + str(count) + string[-1]
    return res

with open('Encript.txt', 'w') as file:
    file.write(Encrypt(string))
    encrypt_string = Encrypt(string)


def Decrypt(encrypt_string):
    decoded_string = ''
    char_amount = ''
    for i in range(len(encrypt_string)):
        if encrypt_string[i].isdigit():
            char_amount += encrypt_string[i]
        else:
            decoded_string += encrypt_string[i] * int(char_amount)
            char_amount = ''

    return decoded_string


with open('Decrypt.txt', 'w') as file:
    file.write(Decrypt(encrypt_string))
print(string)
print(f'Закодированная строка: ' + Encrypt(string))
print(f'Расшифрованная строка: ' + Decrypt(encrypt_string))
