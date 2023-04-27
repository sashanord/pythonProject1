"""Класс Train"""

from datetime import datetime

def simple_hash(val):
    """Простая хэш-функция"""
    seed = 23
    hash = 0
    for i in range(len(val)):
        hash = hash * seed + ord(val[i])
    return hash


def not_so_simple_hash(val):
    """Сложная хэш-функция"""
    b = 3
    a = 5

    hash = 0
    for v in val:
        hash = hash * a + ord(v)
        a = a * b
    return hash




class Train:
    """Класс, описывающий объект поезда """

    def __init__(self, train_name, date, dep_time, trav_time, num, type):
        self.train_name = train_name
        self.date = datetime.strptime(date, '%m/%d/%Y')
        self.dep_time = dep_time
        self.trav_time = trav_time
        self.num = num
        self.type = type

        self.simple_hash = simple_hash(train_name)
        self.not_so_simple_hash = not_so_simple_hash(train_name)

    def __lt__(self, other):
        """Перегрузка оператора <"""
        return self.train_name < other.train_name

    def __le__(self, other):
        """Перегрузка оператора <="""
        return self.train_name <= other.train_name

    def __gt__(self, other):
        """Перегрузка оператора >"""
        return self.train_name > other.train_name

    def __ge__(self, other):
        """Перегрузка оператора >="""
        return self.train_name >= other.train_name

    def __eq__(self, other):
        """Перегрузка оператора =="""
        return self.train_name == other.train_name

