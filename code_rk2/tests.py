import pytest
from func import *

programms = [
    Programm(1, 'Yandex Browser', 167, 1),
    Programm(2, 'Telegram', 366, 1),
    Programm(3, 'Word', 372, 1),
    Programm(4, 'Firefox Browser', 249.5, 2),
    Programm(5, 'VS Code', 238.8, 2),
    Programm(6, 'IDEA Community', 1234, 2),
    Programm(7, 'Drawio', 234.7, 3),
    Programm(8, 'OneNote', 344, 4),
]
 
# Сотрудники
computers = [
    Computer(1, 'PC1'),
    Computer(2, 'PC2'),
    Computer(3, 'PC3'),
    Computer(4, 'PC4'),
]
 
programms_computers = [
    ProgrammComputer(1,1),
    ProgrammComputer(1,2),
    ProgrammComputer(1,3),
    ProgrammComputer(2,4),
    ProgrammComputer(2,5),
    ProgrammComputer(2,6),
    ProgrammComputer(3,7),
    ProgrammComputer(4,8),
    ProgrammComputer(1,7),
    ProgrammComputer(3,6),
    ProgrammComputer(3,2),
    ProgrammComputer(4,5),
    ProgrammComputer(5,6),
]

def test_1():
    otm = one_to_many(computers, programms)
    t1 = task_1(otm)
    assert [el[0] for el in t1] == ['Drawio', 'Firefox Browser', 'IDEA Community', 'OneNote','Telegram', 'VS Code','Word', 'Yandex Browser']

def test_2():
    otm = one_to_many(computers, programms)
    t2 = task_2(computers, otm)
    assert t2 == [('PC1', 3), ('PC2', 3), ('PC3', 1), ('PC4', 1)]

def test_3():
    mtm = many_to_many(computers, programms, programms_computers)
    t3 = [el[0] for el in task_3(mtm)]
    assert 'Telegram' in t3
    assert 'Word' in t3
    assert 'OneNote' in t3
    assert 'IDEA Community' in t3
