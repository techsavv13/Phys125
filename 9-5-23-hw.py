# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 20:39:32 2023

@author: Savvie
"""

import vpython as vpy
import vpvecutils as util

m=.25
pos=vpy.vec(0,2,0)
v=vpy.vec(3,4,0)
fNet=vpy.vec(0,9.8,0)
tInit=0.0
tStep=0.05
tFinal=0.15
now=0.05

print(tInit)
print(pos)
print(v)
print('---------')

for t in range(4):
    print(now)
    Vnow=util.posup(pos,v,now)
    Anow=util.posup(v,fNet,now)
    print('---------')
    now+=tStep
    
'''
print("+++++++++++++++")
while v.y()>-2.0:
    print(now)
    Vnow=util.posup(pos,v,now)
    Anow=util.posup(v,fNet,now)
    print('---------')
    now+=tStep
'''