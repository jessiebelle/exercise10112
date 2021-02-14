#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
print('-' * len(Belgium))
print(Belgium.replace(',', ':'))
x = int(Belgium[8:16])
print(x)
y = int(Belgium[26:32])
print(y)
z=x+y
print(z)