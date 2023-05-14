# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 04:50:07 2022

@author: aravi
"""

import csv
from collections import defaultdict

path = list()

def load_regions(filename):
    states_dict = dict()

    with open(filename, 'r') as f:
        for line in csv.reader(f):
            states_dict[line[1]] = int(line[3])

    return states_dict

def load_borders(filename):
    borders_dict = defaultdict(list)

    with open(filename, 'r') as f:
        for line in csv.reader(f, 1):
            states = line[1].split('-')
            if len(states) == 2:
                borders_dict[states[0]].append(states[1])
                borders_dict[states[1]].append(states[0])
    return borders_dict

def DFS(currentNode, graph,maxDepth,curList):
    #print("Checking for destination",currentNode)
    curList.append(currentNode)
    
    if maxDepth<=0:
        path.append(set(curList))
        return False
    for node in graph[currentNode]:
        if DFS(node,graph,maxDepth-1,curList):
            return True
        else:
            curList.pop()
    return False

def iterativeDDFS(currentNode,graph,maxDepth):
    for i in range(maxDepth):
        curList = list()
        if DFS(currentNode,graph,i,curList):
            return True
    return False

def transform(states, path2, n):
    final_dict = dict()
    for i in path2:
        total = 0
        if len(i) == n:
            for j in i:
                key = states.get(j)
                total += key
                final_dict[total] = i
                
    return tuple([tuple(final_dict[max(tuple(final_dict.keys()))]), max(list(final_dict.keys()))])
            
def new_nation_n_states(n, reg_filename, border_filename):
    
    states = load_regions(reg_filename)
    borders = load_borders(border_filename)
    first = max(states, key=states.get)
    iterativeDDFS(first, borders, n)
    final = transform(states, path, n)
    return final