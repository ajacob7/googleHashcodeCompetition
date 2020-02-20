# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:20:01 2020

@author: Alfredo
"""
def readData(fname):

    f=open(fname, "r")
    f1 = f.readlines()
    f.close()
    
    t=[]
    for i in range(2):
        t.append(f1[i].split())
    
    return t

def printResult(fname, K, pizzas):
    f= open(fname,"w")
    
    t = " ".join(str(x) for x in pizzas)
    f.write(str(K) + "\n")
    f.write(t)
    
    f.close()

def morePizza(fin, fout):
    
    t = readData(fin)
    # M: max number of pizza slices to order
    M = int(t[0][0])
    #Number of different types of pizza
    N = int(t[0][1])
    pizzas = []
    for i in range(N):
        pizzas.append(int(t[1][i]))
        
    res = []
    cur = 0
    for i in range(N-1, -1, -1):
        if pizzas[i] + cur <= M:
            res.insert(0, i)
            cur+=pizzas[i]
        if res== M:
            break
        
    printResult(fout, len(res), res)
    

morePizza("a_example.in", "a_example.out")
morePizza("b_small.in", "b_small.out")
morePizza("c_medium.in", "c_medium.out")
morePizza("d_quite_big.in", "d_quite_big.out")
morePizza("e_also_big.in", "e_also_big.out")