class DataBase:
    def __init__(self, person, inn, address, tax):

        """
        ����������� ������ DataBase

        :param person: ��� ��������
        :type person: str

        :param inn: ��� ��������
        :type inn: int

        :param address: ������ � ������� �����������
        :type address: str

        :param tax: �����
        :type tax: float
        """

        self.person = person
        self.inn = inn
        self.address = address
        self.tax = tax

    def __lt__(self, other):

        """
        ���������� ��������� ������ <

        :param other: ������ ������ :class: 'DataBase', � ������� ���������� ���������
        :type other: :class: 'DataBase'
        :return: True, ���� ������ ������ ������ ������� other, ����� False
        :rtype: bool
        """

        if self.person < other.person:
            return True
        elif self.person == other.person and self.inn < other.inn:
            return True

        return False

    def __gt__(self, other):

        """
        ���������� ��������� ������ >

        :param other: ������ ������ :class: 'DataBase', � ������� ���������� ���������
        :type other: :class: 'DataBase'
        :return: True, ���� ������ ������ ������ ������� other, ����� False
        :rtype: bool
        """

        return not self.__le__(other)

    def __le__(self, other):

        """
        ���������� ��������� ������ ���� ����� <=

        :param other: ������ ������ :class: 'DataBase', � ������� ���������� ���������
        :type other: :class: 'DataBase'
        :return: True, ���� ������ ������ ������ ������� other ��� ����� ���, ����� False
        :rtype: bool
        """

        return self.__lt__(other) or (self.person == other.person and
                                      self.inn == other.inn)

    def __ge__(self, other):

        """
        ���������� ��������� ������ ���� ����� >=

        :param other: ������ ������ :class: 'DataBase', � ������� ���������� ���������
        :type other: :class: 'DataBase'
        :return: True, ���� ������ ������ ������ ������� other ��� ����� ���, ����� False
        :rtype: bool
        """

        return self.__lt__(other)

    def __str__(self):

        """
        ��������� ������������� �������

        :return: ��������� ������������� ������� ������ :class: 'DataBase'
        :rtype: str
        """

        return self.person + "-" + str(self.inn) + "-" + self.address + "-" + str(self.tax)

    def __repr__(self):
        return self.__str__()

