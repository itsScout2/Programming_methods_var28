from sorts import insertion_sort
from DB_class import DataBase
import time
import csv
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)


def linear_search(array: list, element: str) -> list:
    result = []
    for i in array:
        if i.person == element:
            result.append(array.index(i))
    return result


def binary_search(array: list, element: str, start, end) -> list :
    if start > end:
        return []

    result = []
    mid = start + int((start + end)/2)
    if array[mid].person == element:
        result.append(mid)
    elif array[mid].person > element:
        result = binary_search(array, element, start, mid-1)
    elif array[mid].person < element:
        result = binary_search(array, element, mid+1, end)

    if len(result) != 1:
        return result

    left = result[0] - 1
    right = result[0] + 1

    while (left >= 0) and (right < len(array)):
        if array[left].person == element:
            result.insert(0, left)
            left -= 1
        if array[right].wedding_date == element:
            result.append(right)
            right += 1
        else:
            return result

    return result


def insertion_and_binary(array: list) -> list:
    out = insertion_sort(array)
    result = binary_search(out, out[-7].person, 0, len(out)-1)
    return result


if __name__ == '__main__':
    N = [100, 500, 1000, 2500, 5000, 10000, 25000, 50000, 100000]

    for i in N:
        arr = []
        with open(f'insertion_sort_{i}.csv', mode='r') as r_file:
            file_reader = csv.reader(r_file, delimiter="-", lineterminator="\r")

            for row in file_reader:
                tmp = []
                if row[0] == '‘»Œ':
                    continue
                str_row = row[0] + '-' + row[1] + '-' + row[2] + '-' + row[3]
                line = str_row.split('-')
                tmp.append(DataBase(*line))
                arr.append(tmp)
    # TODO finish with task and compare times