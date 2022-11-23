def show_menu():
    print('Выберите действие')
    print('1 -Добавить сотрудника')
    print('2 -Обновить данные сотрудника')
    print('3 -Печать таблицы')
    print('4 -Печать данных сотрудника')
    print('5 -Удалить данные сотрудника')
    print('6 -Изменить номер телефона сотрудника')

    return input('Введите цифру: ')

def add_info():
    a = input('Введите фамилию: ')
    b = input('Введите имя: ')
    c = input('Введите номер телефона: ')
    d = input('Введите комментарий: ')
    user = (a, b, c, d )
    return user

def get_index():
    index = input('Введите id сотрудника: ')
    return index

def get_tel():
    tel = input('Введите номер телефона: ')
    return tel

def apdate_info():
    lastname = input('Введите фамилию: ')
    return lastname
