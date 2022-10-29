from classes.programm import Programm
from classes.computer import Computer
from classes.programm_computer import ProgrammComputer

from operator import itemgetter

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
 
def main():
 
    # Соединение данных один-ко-многим 
    one_to_many = [(p.name, p.size_MB, c.name) 
        for c in computers
        for p in programms 
        if p.computer_id==c.id]
    
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(c.id, c.name, pc.programm_id) 
        for c in computers
        for pc in programms_computers
        if c.id==pc.computer_id]
    
    many_to_many = [(p.name, p.size_MB, c_name) 
        for p in programms
        for c_id, c_name, p_id in many_to_many_temp 
        if p.id==p_id]
 
    print('Задание 1')
    task_1 = sorted(one_to_many, key=itemgetter(0))
    for el in task_1:
        print(el)
    print('Задание 2')
    task_2 = []
    for i in range(len(computers)):
        cnt_programms = 0
        for j in one_to_many:
            if(j[2] == computers[i].name):
                cnt_programms += 1
        task_2.append((computers[i].name, cnt_programms))
    task_2 = sorted(task_2, key=itemgetter(1), reverse=True)
    for el in task_2:
        print(el)
    print('Задание 3')
    task_3 = []
    for el in many_to_many:
        if(el[1] > 300):
            task_3.append(el)
    for el in task_3:
        print(el)
    
 
if __name__ == '__main__':
    main()
