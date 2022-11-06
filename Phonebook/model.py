import csv
from encodings import utf_8

# чтение файла csv
def read_csv():
    with open('Phonebook/phonebook.csv', encoding = 'utf_8') as f:
        reader = csv.reader(f, delimiter =',')
        
        res = list(reader)
        return res


# запись в файл csv
def write_csv(row):
    with open('Phonebook/phonebook.csv',mode = "a", encoding = 'utf_8', newline= '') as f:
        writer = csv.writer(f, delimiter =',', lineterminator = "\n")
        writer.writerow(row)
        
        
# чтение файла txt    



# Считываем и возвращаем считанные данные с файла
def readFile():
    with open('Phonebook/phonebook.txt', 'r', encoding='utf-8') as f:
        data_txt = f.read()
        print(data_txt)

# Записываем текст в файл
def writeFile(row):
    with open('Phonebook/phonebook.txt', 'a', encoding='utf-8', newline= '\r') as f:
        f.write(row + '\n')




# запись в файл txt
    