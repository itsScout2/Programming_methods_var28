class DataBase:
    def __init__(self, person, inn, address, tax):

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
        """

        self.person = person
        self.inn = inn
        self.address = address
        self.tax = tax

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

