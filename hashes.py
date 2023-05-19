# -*- coding: cp1251 -*-
import pandas as pd
import csv
import timeit
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 400)

def JS_hash(key: str) -> int:
    hash = 1315423911
    for i in range(len(key)):
        hash ^= ((hash << 5) + ord(key[i]) + (hash >> 2))
        hash %= (1 << 20)
    return hash

def LY_hash(key: str) -> int:
    hash = 0
    for i in range(len(key)):
        hash = (hash * 1664525) + ord(key[i]) + 1013904223
        hash %= (1 << 20)
    return hash


class DataBase_hash:
    def __init__(self, person, inn, address, tax, hash_f=JS_hash):

        """
        Конструктор класса DataBase

        :param person: ФИО человека
        :type person: str

        :param inn: ИНН человека
        :type inn: int

        :param address: Строка с адресом регистрации
        :type address: str

        :param tax: Налог
        :type tax: float

        :param hash_f: Выбор хэш функции
        :type none
        """

        self.person = person
        self.inn = inn
        self.address = address
        self.tax = tax
        self.hash = hash_f(self.person)

    def __lt__(self, other):

        """
        Перегрузка оператора меньше <

        :param other: Объект класса :class: 'DataBase', с которым происходит сравнение
        :type other: :class: 'DataBase'
        :return: True, если данный объект меньше объекта other, иначе False
        :rtype: bool
        """

        if self.person < other.person:
            return True
        elif self.person == other.person and self.inn < other.inn:
            return True

        return False

    def __gt__(self, other):

        """
        Перегрузка оператора больше >

        :param other: Объект класса :class: 'DataBase', с которым происходит сравнение
        :type other: :class: 'DataBase'
        :return: True, если данный объект больше объекта other, иначе False
        :rtype: bool
        """

        return not self.__le__(other)

    def __le__(self, other):

        """
        Перегрузка оператора меньше либо равно <=

        :param other: Объект класса :class: 'DataBase', с которым происходит сравнение
        :type other: :class: 'DataBase'
        :return: True, если данный объект меньше объекта other или равен ему, иначе False
        :rtype: bool
        """

        return self.__lt__(other) or (self.person == other.person and
                                      self.inn == other.inn)

    def __ge__(self, other):

        """
        Перегрузка оператора больше либо равно >=

        :param other: Объект класса :class: 'DataBase', с которым происходит сравнение
        :type other: :class: 'DataBase'
        :return: True, если данный объект больше объекта other или равен ему, иначе False
        :rtype: bool
        """

        return self.__lt__(other)

    def __str__(self):

        """
        Строковое представление объекта

        :return: Строковое представление объекта класса :class: 'DataBase'
        :rtype: str
        """

        return self.person + "-" + str(self.inn) + "-" + self.address + "-" + str(self.tax)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return self.hash

def add_to_hash(hash_array: dict, element: DataBase_hash):
    if hash_array.get(element.hash) is None:
        hash_array[element.hash] = element
    elif isinstance(hash_array[element.hash], list):
        hash_array[element.hash].append(element)
    else:
        hash_array[element.hash] = [hash_array[element.hash], element]

def get_from_hash(hash_array: dict, key: str, hash_f=JS_hash):
    if isinstance(hash_array.get(hash_f(key)), list):
        for i in hash_array[hash_f(key)]:
            if i.person == key:
                return i
        return -1
    else:
        return hash_array.get(hash_f(key), -1)

def collisions(hash_array: dict):
    cnt = 0
    for i in hash_array.values():
        if isinstance(i, list):
            cnt += len(set(i)) - 1
    return cnt

if __name__ == '__main__':
    N = [100, 500, 1000, 2500, 5000, 10000, 25000, 50000, 100000]
    delta_time_JS_hash = []
    delta_time_LY_hash = []
    collisions_JS_hash = []
    collisions_LY_hash = []
    dict_JS = {}
    dict_LY = {}

    for i in N:
        with open(f'DB_{i}.csv', mode='r') as r_file:
            file_reader = csv.reader(r_file, delimiter="-", lineterminator="\r")

            for row in file_reader:
                tmp_JS = []
                tmp_LY = []
                if row[0] == 'ФИО':
                    continue
                str_row = row[0] + '-' + row[1] + '-' + row[2] + '-' + row[3]
                line = str_row.split('-')
                tmp_JS.append(DataBase_hash(*line))
                tmp_LY.append(DataBase_hash(*line, hash_f=LY_hash))
                add_to_hash(dict_JS, tmp_JS[0])
                add_to_hash(dict_LY, tmp_LY[0])

        key = line[0]

        #delta_time_JS_hash.append(timeit.Timer(lambda: get_from_hash(dict_JS, key)).timeit(number=1))
        #delta_time_LY_hash.append(timeit.Timer(lambda: get_from_hash(dict_LY, key)).timeit(number=1))

        collisions_JS_hash.append(collisions(dict_JS))
        collisions_LY_hash.append(collisions(dict_LY))

    #d_hashes = {'Время поиска для простой хэш-функции': delta_time_JS_hash,
    #            'Время поиска для сложной хэш-функции': delta_time_LY_hash}
    #df_hashes = pd.DataFrame(data=d_hashes, index=N)
    #print(df_hashes)
    #print('\n\n\n')

    d_collisions = {'Кол-во коллизий простой хэш-функции': collisions_JS_hash,
                    'Кол-во коллизий сложной хэш-функции': collisions_LY_hash}
    df_collisions = pd.DataFrame(data=d_collisions, index=N)
    print(df_collisions)



