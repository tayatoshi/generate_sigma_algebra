"""
最小なシグマ加法族の生成
"""

import numpy as np
import copy as cp
import itertools


omega = list(set([1,2,3,4,5,6]))
F =list(set([1,3,6]))
geneF = []
print('Ω :',omega)
print('F:',F)
print('----------------------')
print('F*:')
def get_Ac(f):
    if f != omega:
        A_c = cp.deepcopy(omega)
        for i in range(len(f)):
            A_c.remove(f[i])
    return A_c

def get_subset(f):
    A = f
    A_c = get_Ac(f)
    return A, A_c

for i in range(len(F)+1):
    if i ==0:
        result = ('φ ' ,omega)
        for k in range(2):
            geneF.append(result[k])
        print(result)
    elif i!=len(omega):
        comb = list(itertools.combinations(F,i))
        for j in range(len(comb)):
            result = get_subset(list(comb[j]))
            for k in range(2):
                geneF.append(result[k])
            print(result)
