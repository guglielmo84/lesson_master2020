#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 17:18:43 2020

@author: user
"""

print ("Esempio di LIST")
print ("i delimitatori di una lista sono le parentesi quadre")
mylist = ['byte', 3.1415, 2+1j]
print ("usiamo l'INDICIZZAZXIONE, Le posizioni iniziano da 0. Il primo elemanto sara maylist di 0, l'ultimo elemento sarà -1")
print (mylist)
print (mylist[0],mylist[-1])
print ("Estrarre un sottinsieme di elemti contigui")
print (mylist[0:2])
print (mylist[0:-1])
print ("Prendere il prefisso o un suffisso di una lista")
print (mylist[:2])
print (mylist[2:])


print ("MANIPOLAZIONI DI LIST")
print ("creo un alias, due nomi diversi per lo stesso oggetto")
a=mylist
print ("prendiamo due liste e applichiamo l'operatore +, che fa un append")
a = a + ['hello']


print("modificare la lista con il comando append, che non muta l'indirizzo di memoria. 'si dice che append è un metodo di list'")
print (id(a))
a.append("2L")
print (id(a))

print("mylst prima e dopo il del \n", mylist)
del mylist[1]
print(mylist)

print ("concatenazione in-place, cie che non cambia l'identita")


b=[4,5,-2,6,1.2]
b.sort()
print(id(b))
c=b
print(id(c))
c= sorted(b)
print(id(c))
d = [0,1]

a[1] =b
f=[2]
a[2] = f

del a,b,c,d,f


#UPLA
print("**************************************************")

print("********************TUPLA*************************")
print("**************************************************")

print ("le tuple sono immutable")
print ("le tuple si dichiarano con le tonde")

monkeys = ['joe','jack']
zoo=('lion', 'tiger', monkeys)

zoo2=zoo

del zoo

monkeys.append('jim')




























