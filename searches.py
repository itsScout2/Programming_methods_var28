# -*- coding: cp1251 -*-
from sorts import insertion_sort
from DB_class import DataBase
import timeit
import csv
import pandas as pd
from collections import defaultdict
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 400)
pd.options.display.float_format = '{:.10f}'.format

def linear_search(array: list, element: str) -> list:

    """
    Реализация линейного поиска

    :param array: Массив для поиска
    :type array: list
    :param element: эталонный элемент, который надо найти
    :type element: str
    :return: список - индексы совпадающих элементов массива с element
    :rtype: list
    """

    result = []
    for i in array:
        if i[0].person == element:
            result.append(array.index(i))
    return result


def binary_search(array: list, element: str, start, end) -> list :

    """
    Реализация бинарного поиска

    :param array: Массив для поиска
    :type array: list
    :param element: эталонный элемент, который надо найти
    :type element: str
    :param start: индекс элемента, с которого начинается поиск
    :type start: int
    :param end: индекс элемента, на котором закончить поиск
    :type end: int
    :return: список - индексы совпадающих элементов массива с element
    :rtype: list
    """

    if start > end:
        return []

    result = []
    mid = int((start + end)/2)
    if array[mid][0].person == element:
        result.append(mid)
    elif array[mid][0].person > element:
        result = binary_search(array, element, start, mid-1)
    elif array[mid][0].person < element:
        result = binary_search(array, element, mid+1, end)

    if len(result) != 1:
        return result

    left = result[0] - 1
    right = result[0] + 1

    while (left >= 0) and (right < len(array)):
        if array[left][0].person == element:
            result.insert(0, left)
            left -= 1
        if array[right][0].person == element:
            result.append(right)
            right += 1
        else:
            return result

    return result


def insertion_and_binary(array: list) -> list:

    """
    Реализация сортировки простыми вставками и бинарный поиск
                                    в отсортированном массиве

    :param array: Массив для сортировки
    :type array: list
    :return: список - индексы совпадающих элементов массива с element
    :rtype: list
    """

    out = insertion_sort(array)
    result = binary_search(out, out[-7][0].person, 0, len(out)-1)
    return result


if __name__ == '__main__':
    N = [100, 500, 1000, 2500, 5000, 10000, 25000, 50000, 100000]

    delta_time_linear = []
    delta_time_binary = []
    delta_time_ins_and_bin = []
    time_multimap = []

    for i in N:
        arr = []
        with open(f'insertion_sort_{i}.csv', mode='r') as r_file:
            file_reader = csv.reader(r_file, delimiter="-", lineterminator="\r")

            for row in file_reader:
                tmp = []
                if row[0] == 'ФИО':
                    continue
                tmp_row = str(row[0]).split('-')
                tmp.append(DataBase(*tmp_row))
                arr.append(tmp)


        delta_time_linear.append(timeit.Timer(lambda: linear_search(arr.copy(),
                                            arr[-7][0].person)).timeit(number=1))
        delta_time_binary.append(timeit.Timer(lambda: binary_search(arr.copy(),
                            arr[-7][0].person, 0, len(arr) - 1)).timeit(number=1))

        arr1 = []
        with open(f'DB_{i}.csv', mode='r') as r_file:
            file_reader = csv.reader(r_file, delimiter="-", lineterminator="\r")

            for row in file_reader:
                tmp = []
                if row[0] == 'ФИО':
                    continue
                str_row = row[0] + '-' + row[1] + '-' + row[2] + '-' + row[3]
                line = str_row.split('-')
                tmp.append(DataBase(*line))
                arr1.append(tmp)

        #delta_time_ins_and_bin.append(timeit.Timer(lambda: insertion_and_binary(arr1.copy())).timeit(number=1))
        DB_dict = defaultdict(list)
        for i in arr1:
            DB_dict[i[0].person].append(i[0])
        time_multimap.append(timeit.Timer(lambda: DB_dict[arr1[-1][0].person]).timeit(number=1))

    d = {'Время поиска линейным поиском': delta_time_linear,
        'Время поиска бинарным поиском': delta_time_binary,
        'Время поиска бинарным поиском вместе с сортировкой': delta_time_ins_and_bin}

    df = pd.DataFrame(data=d, index=N)
    print(df)
    d_multimap = {'Время поиска по ключу': time_multimap}
    df_multimap = pd.DataFrame(data=d_multimap, index=N)
    print(df_multimap)
