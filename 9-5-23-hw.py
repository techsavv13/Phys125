# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 20:39:32 2023

@author: Savvie
"""
#default import block
import vpython as vpy
import vpvecutils as util
import numpy as np 

#base values
m=.25
pos=vpy.vec(0,2,0)
v=vpy.vec(3,4,0)
fNet=vpy.vec(0,9.8,0)
tInit=0.0
tStep=0.05
tFinal=0.2
now=0.05

#initial print
print(tInit)
print(pos)
print(v)
print('---------')

#for i in np.arange(-3.14, 3.14, 0.1): print (i)

#loop
for t in np.arange(now,tFinal,tStep):
    print(t)
    Vnow=util.posup(pos,v,t)
    Anow=util.posup(v,fNet,t)
    print('---------')
    #now+=tStep
    
'''
don't worry about it
print("+++++++++++++++")
while v.y()>-2.0:
    print(now)
    Vnow=util.posup(pos,v,now)
    Anow=util.posup(v,fNet,now)
    print('---------')
    now+=tStep
'''