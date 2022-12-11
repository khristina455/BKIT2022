import json
import sys
from cm_timer import cm_timer_1, cm_timer_2
from print_result import print_result
from unique import Unique
from field import field
from gen_random import gen_random

# Сделаем другие необходимые импорты

path = "data_light.json"

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

with open(path) as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
    return sorted(list(Unique(field(arg, "job-name"), ignore_case = True)))


@print_result
def f2(arg):
    return list(filter(lambda s: s[:11].lower() == "программист", arg))


@print_result
def f3(arg):
    return list(map(lambda s: s + " c опытом Python", arg))


@print_result
def f4(arg):
    gen = gen_random(len(arg), 100000, 200000)
    return list(zip(arg, ["зарплата " + str(i) + " руб" for i in gen]))


if __name__ == '__main__':
    with cm_timer_1():
       f4(f3(f2(f1(data))))