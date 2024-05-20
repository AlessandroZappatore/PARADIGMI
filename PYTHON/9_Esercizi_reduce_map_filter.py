
#%%
# 1. Scrivere la funzione fattoriale(n) usando la funzione reduce (senza iterazione
#    o ricorsione).
from functools import reduce
import operator 
def fattoriale(n):
    return reduce(operator.imul,range(1, n+1), 1)
#%%
# 2. Scrivi una list comprehension equivalente a:

list(map(lambda x: x**3,(filter(lambda x: x % 5 != 0, range(3,20,3)))))
[x**3 for x in range(3, 20, 3) if x%5!=0]
#%%
# 4. Scrivi la seguente list comprehension utilizzando map e filter:

[x[1] - x[0] for x in enumerate(range(20,3,-1)) if x[1] != 7]  
list(map(lambda x: x[1]-x[0], (filter(lambda x:x[1]!=7, enumerate(range(20, 3, -1))))))
#%%
# 3.  Usando map e zip scrivere una funzione diff(seq) che data una sequenza di 
#    interi genera la sequenza delle differenze degli elementi adiacenti.
#    Ad esempio
#      diff([3,2,7,4,4]) => [1,-5,3,0]
def diff(seq):
    return list(map(lambda x:x[0]-x[1], zip(seq, seq[1:])))

#%%
# 4. Scrivere una funzione contaVocali(str) che ritorna una quintupla (nA,nE,nI,nO,nU) 
# contenente il numero di a, e, i,o ,u  della stringa. Usare la funzione foldLeft
def foldLeft(lis,init,fn):
    acc = init
    for x in lis:
        acc = fn(acc,x)
    return acc
# Ad esempio 
#     contaVocali("abeiarc") ==>  (2,1,1,0,0)
