# -*- coding: cp1251 -*-
from DB_class import DataBase
import time
import csv
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)


def selection_sort(array: list) -> list:

    """
    ���������� ���������� �������

    :param array: ������ ��� ����������
    :type array: list
    :return: ��������������� ������
    :rtype: list
    """

    for i in range(len(array) - 1):
        min = i
        for j in range(i + 1, len(array)):
            if (array[j] < array[min]):
                min = j
        array[i], array[min] = array[min], array[i]

    return array


def bubble_sort(array: list) -> list:

    """
    ���������� ���������� '���������'

    :param array: ������ ��� ����������
    :type array: list
    :return: ��������������� ������
    :rtype: list
    """

    has_swapped = True

    while has_swapped:
        has_swapped = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                has_swapped = True
    return array


def insertion_sort(array: list) -> list:

    """
    ���������� ���������� �������� ���������

    :param array: ������ ��� ����������
    :type array: list
    :return: ��������������� ������
    :rtype: list
    """

    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while (j >= 0 and temp < array[j]):
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = temp

    return array


if __name__ == '__main__':
    N = [100, 500, 1000, 2500, 5000, 10000, 25000, 50000, 100000]

    for i in N:
        arr = []
        with open(f'DB_{i}.csv', mode='r') as r_file:
            file_reader = csv.reader(r_file, delimiter="-", lineterminator="\r")

            for row in file_reader:
                tmp = []
                if row[0] == '���':
                    continue
                str_row = row[0] + '-' + row[1] + '-' + row[2] + '-' + row[3]
                line = str_row.split('-')
                tmp.append(DataBase(*line))
                arr.append(tmp)

            start_time_selection = time.time()
            selection_arr = selection_sort(arr.copy())
            end_time_selection = time.time()

            delta_time_selection = []
            delta_time_selection.append((end_time_selection - start_time_selection) * 10 ** 3)
            with open(f'selection_sort_{i}.csv', mode='w') as w_file:
                file_writer = csv.writer(w_file, delimiter="-", lineterminator="\r")
                header = ["���", "���", "����� �����������", "����� ����������� ������ �� ������� ���"]
                file_writer.writerow(header)
                file_writer.writerows(selection_arr)

            start_time_bubble = time.time()
            bubble_arr = bubble_sort(arr.copy())
            end_time_bubble = time.time()

            delta_time_bubble = []
            delta_time_bubble.append((end_time_bubble - start_time_bubble) * 10 ** 3)
            with open(f'buble_sort_{i}.csv', mode='w') as w_file:
                file_writer = csv.writer(w_file, delimiter="-", lineterminator="\r")
                header = ["���", "���", "����� �����������", "����� ����������� ������ �� ������� ���"]
                file_writer.writerow(header)
                file_writer.writerows(bubble_arr)

            start_time_insertion = time.time()
            insertion_arr = insertion_sort(arr.copy())
            end_time_insertion = time.time()

            delta_time_insertion = []
            delta_time_insertion.append((end_time_insertion - start_time_insertion) * 10 ** 3)
            with open(f'insertion_sort_{i}.csv', mode='w') as w_file:
                file_writer = csv.writer(w_file, delimiter="-", lineterminator="\r")
                header = ["���", "���", "����� �����������", "����� ����������� ������ �� ������� ���"]
                file_writer.writerow(header)
                file_writer.writerows(insertion_arr)

    d = {'����� ���������� �������':delta_time_selection,
         '����� ���������� ���������':delta_time_bubble,
         '����� ���������� �������� ���������':delta_time_insertion}

    df = pd.DataFrame(data=d, index=N)
    print(df)
