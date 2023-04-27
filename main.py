"""Основные функции"""

import random
import timeit

import pandas as pd
from collections import deque

from find_algorithms import simple_search
from find_algorithms import binary_search
from find_algorithms import quick_sort
from collections import defaultdict

from Train import Train
from generation import generate

"""Размерность сгенерированных наборов данных"""
nums = [100_000, 200_000, 300_000, 400_000, 500_000, 600_000, 700_000]
trains = {}

collisions_simple = []
collisions_not_so_simple = []

hash_time_sim = []
hash_time_not_sim = []

time_spent_simple = []
time_spent_binary_sort = []
time_spent_binary = []
time_spent_key = []


def write_in_file():
    """Запись сгенерированных файлов в файл"""
    with pd.ExcelWriter("./trains.xlsx") as writer:
        for i in nums:
            pd.DataFrame(generate(i)).to_excel(writer, sheet_name=f"{i}", index=False)

def write_in_dict():
    """Чтение из файла и запись в словарь, для дальнейшей сортировки"""
    for i in nums:
        curr = pd.read_excel('./trains.xlsx', sheet_name=f'{i}').to_dict('records')
        curr_trains = []
        for train in curr:
            curr_trains.append(
                Train(train['Имя поезда'], train['Дата отправления'], train['Время отправления'], train['Время в пути'],
                      train['Номер поезда'],
                      train['Тип поезда'])
            )
        trains[i] = curr_trains



if __name__ == '__main__':

    # write_in_file()
    write_in_dict()

    for i in nums:
        col_simp = 0
        coll_not_simp = 0
        table_simple_hash = {}
        table_not_so_simple_hash = {}
        """Создание хэш-таблицы методом цепочек"""
        for j in range(i):
            sim = trains[i][j].simple_hash
            not_sim = trains[i][j].not_so_simple_hash

            """Создание таблицы с простой хэш-функцией"""
            if sim not in table_simple_hash:
                table_simple_hash[sim] = deque()
            else:
                for t in table_simple_hash[sim]:
                    if trains[i][j].train_name == t.train_name:
                        break
                else:
                    col_simp += 1
            table_simple_hash[sim].append(trains[i][j])

            # Создание таблицы со сложной хэш-функцией
            if not_sim not in table_not_so_simple_hash:
                table_not_so_simple_hash[not_sim] = deque()
            else:
                for t in table_not_so_simple_hash[not_sim]:
                    if trains[i][j].train_name == t.train_name:
                        break
                else:
                    coll_not_simp += 1
            table_not_so_simple_hash[not_sim].append(trains[i][j])

        collisions_simple.append(col_simp)
        collisions_not_so_simple.append(coll_not_simp)

        """Поиск в хэш таблицах"""
        names = [k.train_name for k in trains[i]]
        key = Train(random.choice(names), "01/01/2000", "", "", "", "")

        start = timeit.default_timer()
        items = table_simple_hash[key.simple_hash]
        for item in items:
            if item == key:
                print(item)
                break
        end = timeit.default_timer() - start
        hash_time_sim.append(end)

        # Поиск в сложной
        start = timeit.default_timer()
        items = table_not_so_simple_hash[key.not_so_simple_hash]
        for item in items:
            if item == key:
                print(item.train_name)
                break
        end = timeit.default_timer() - start
        hash_time_not_sim.append(end)

        """Поиск по ключу в массиве"""
        train_multi_map = defaultdict(list)
        for train in trains[i]:
            train_multi_map[train.train_name].append(train)
        starttime1 = timeit.default_timer()
        print(train_multi_map[key.train_name])
        end1 = timeit.default_timer() - starttime1
        time_spent_key.append(end1)

        """Простой поиск"""
        starttime2 = timeit.default_timer()
        simple_search(trains[i], key)
        end2 = timeit.default_timer() - starttime2
        time_spent_simple.append(end2)

        """Бинарный поиск с сортировкой"""
        starttime3 = timeit.default_timer()
        quick_sort(trains[i], 0, len(trains[i]) - 1)
        binary_search(trains[i], 0, len(trains[i]), key)
        end3 = timeit.default_timer() - starttime3
        time_spent_binary_sort.append(end3)

        """Бинарный поиск"""
        starttime4 = timeit.default_timer()
        binary_search(trains[i], 0, len(trains[i]), key)
        end4 = timeit.default_timer() - starttime4
        time_spent_binary.append(end4)

    print(f'hash_time_sim = {hash_time_sim}')
    print(f'hash_time_not_sim = {hash_time_not_sim}')

    print(f'collisions_simple = {collisions_simple}')
    print(f'collisions_not_so_simple = {collisions_not_so_simple}')

    print(f'time_spent_simple = {time_spent_simple}')
    print(f'time_spent_binary_sort = {time_spent_binary_sort}')
    print(f'time_spent_binary = {time_spent_binary}')
    print(f'time_spent_key = {time_spent_key}')


