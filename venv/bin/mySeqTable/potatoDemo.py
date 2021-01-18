# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 13:05:18 2020

@author: 22169
"""


def hotPotato(namelist, num):
    simqueue = []
    for name in namelist:
        simqueue.append(name)
    
    while len(simqueue) > 1:
        for i in range(num):
            simqueue.append(simqueue.pop(0))
        simqueue.pop(0)
    
    return simqueue.pop(0)

if __name__ == "__main__":
    namelist = [i for i in range(40)]
    print(hotPotato(namelist, 7))