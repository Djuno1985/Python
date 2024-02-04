"""Задача №49. Решение в группах Создать телефонный справочник с
возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
60 минут
"""
from csv import DictReader, DictWriter
from os.path import exists


class NameError:
    def __init__(self, txt):
        self.txt = txt


class PhoneError:
    def __init__(self, txt):
        self.txt = txt


def get_user_data():  # функция запрашивает данные
    flag = False
    while not flag:
        try:
            first_name = input('Введите имя: ')
            if len(first_name) < 2:
                raise NameError('Невалидная длина')
            last_name = input('Введите фамилию: ')
            phone_number = int(input('Введите телефон: '))
            if len(str(phone_number)) < 11:
                raise PhoneError('Не верная длинна номера')
            flag = True
        except ValueError:
            print('Вы вводите символы вместо цыфр')
            continue
        except NameError as err:
            print(err)
            continue
        except PhoneError as err:
            print(err)
            continue
    return first_name, last_name, phone_number


def create_file(file_name):  # создание файла
    with open(file_name, 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()


file_name = 'phon.csv'


def read_file(file_name):  # чтение файла
    with open(file_name, encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)


def write_file(file_name):  # запись файла
    user_data = get_user_data()
    res = read_file(file_name)
    for el in res:
        if el['Телефон'] == str(user_data[2]):
            print('Такой номер уже существует!')
            return
    obj = {'Имя': user_data[0], 'Фамилия': user_data[1], 'Телефон': user_data[2]}
    res.append(obj)
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)


def copy_file(file_name, file_name_new):
    list_1 = read_file(file_name)

    y = int(input(f"Выберите номер строки от 1 до {len(list_1)}: "))

    if 1 <= y <= len(list_1):
        obj = list_1[y - 1]
        res = [obj]

        with open(file_name_new, 'w', encoding='utf-8', newline='') as data:
            fieldnames = ['Имя', 'Фамилия', 'Телефон']
            f_writer = DictWriter(data, fieldnames=fieldnames)
            f_writer.writeheader()
            f_writer.writerows(res)

        print(f'Строка {y} успешно скопирована из {file_name} в {file_name_new}')
    else:
        print('Неверный номер строки')


def main():  # диспетчер
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name)
            print('Данные успешно записаны')
        elif command == 'r':
            if not exists(file_name):
                print('Файл не создан! Создайте его')
                continue
            print(read_file(file_name))
        elif command == 'c':
            if not exists(file_name):
                print('Файл не создан! Создайте его!')
                continue
            new_file_name = input('Введите имя нового файла: ')
            copy_file(file_name, new_file_name)
            print(f'Данные успешно скопированы в {new_file_name}')


main()
