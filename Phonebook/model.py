

import csv
from encodings import utf_8

# чтение файла csv
with open('phonebook.csv', encoding = utf_8) as f:
    f_reader = csv.reader(f, delimiter =',')
    count = 0
    for row in f_reader:
        if count == 0:
            print(','.join(row))
        else:
            print(row)
        count += 1
        
# запись в файл csv
with open('phonebook.csv',mode = "w", encoding = utf_8) as f:
    f_writer = csv.writer(f, delimiter =',', lineterminator = "\r")
    count = 0
    for row in f_reader:
        if count == 0:       
            f_writer.writerow(["Имя"], ["Фамилия"], ["Номер телефона"])
        else:
            f_writer.writerow()
        count += 1
        
        
# чтение файла txt    

#with open('phonebook.txt') as f:
#    f.readlines()

# Считываем и возвращаем считанные данные с файла
def readFile(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.read()
    return data

# Записываем текст в файл
def writeFile(file_name, string):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(string)




# запись в файл txt
    