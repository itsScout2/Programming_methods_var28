import csv
import random
from faker import Faker
from russian_names import RussianNames

fake = Faker(locale="ru_RU")

def generate_rows(n):

    """
    Генерирует список из n списков вида ['ФИО', 'ИНН', 'Адрес регистрации', 'Сумма уплаченного налога за текущий год']

    :param n: Количество генерируемых записей
    :type n: int
    :return: список из n списков вида ['ФИО', 'ИНН', 'Адрес регистрации', 'Сумма уплаченного налога за текущий год']
    :rtype: list[list]
    """

    rows_list = []
    for _ in range(n):
        l = []
        inn = random.randint(0, 999999999999)
        tax = round(random.uniform(0, 150000), 2)
        tmp = RussianNames().get_person().split()
        person = tmp[2] + ' ' + tmp[0] + ' ' + tmp[1]
        address = fake.address()
        l.extend((person, inn, address, tax))
        rows_list.append(l)
    return rows_list


if __name__ == "__main__":
    N = [100, 500, 1000, 2500, 5000, 10000, 25000, 50000, 100000]
    for i in N:
        with open(f'DB_{i}.csv', mode='w') as w_file:
            file_writer = csv.writer(w_file, delimiter="-", lineterminator="\r")
            header = ["ФИО", "ИНН", "Адрес регистрации", "Сумма уплаченного налога за текущий год"]
            file_writer.writerow(header)
            file_writer.writerows(generate_rows(i))
