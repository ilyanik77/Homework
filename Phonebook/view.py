def show_menu():
    print('Выберите действие')
    print('1 - показать TXT файл')
    print('2 - показать CSV файл')
    print('3 - добавить в TXT файл')
    print('4 - добавить в CSV файл')

    return input('Введите цифру: ')

def show_res(res):
    for i, row in enumerate(res):
        print(i, ' '.join(row))


def add_info():
    print('Введите ФИО и тел через пробел')
    in_info = input().split()
    return in_info

def add_txt():
    print('Введите ФИО и тел через запятую')
    in_info = input()
    return in_info

