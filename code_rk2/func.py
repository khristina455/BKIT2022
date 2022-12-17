from classes.programm import Programm
from classes.computer import Computer
from classes.programm_computer import ProgrammComputer

from operator import itemgetter


def one_to_many(computers, programms):
    ans = [(p.name, p.size_MB, c.name) 
        for c in computers
        for p in programms 
        if p.computer_id==c.id]
    return ans

def many_to_many(computers, programms, programms_computers):
    many_to_many_temp = [(c.id, c.name, pc.programm_id) 
        for c in computers
        for pc in programms_computers
        if c.id==pc.computer_id]
    
    ans = [(p.name, p.size_MB, c_name) 
        for p in programms
        for c_id, c_name, p_id in many_to_many_temp 
        if p.id==p_id]
    return ans

def task_1(otm):
    return sorted(otm, key=itemgetter(0))

def task_2(computers, otm):
    ans = []
    for i in range(len(computers)):
        cnt_programms = 0
        for j in otm:
            if(j[2] == computers[i].name):
                cnt_programms += 1
        ans.append((computers[i].name, cnt_programms))
    ans = sorted(ans, key=itemgetter(1), reverse=True)
    return ans

def task_3(mtm):
    ans = []
    for el in mtm:
        if(el[1] > 300):
            ans.append(el)
    return ans
