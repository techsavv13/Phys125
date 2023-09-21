# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 12:28:56 2023

@author: Savvie
"""


import vpython as vpy
import vpvecutils as util
import numpy as np 
import math as math



#q4
def gammaV(v,c=util.c()):
    return(1/math.sqrt(1-((vpy.mag(v)/c)**2)))

mPhone=0.2215
hDennis=12.2
vIip=vpy.vec(3.7,2.1,-1.6)
pIp=gammaV(vIip)*mPhone*vIip
fNet=vpy.vec(0,-9.8,0)
dt=0.6
posPhone=vpy.vec(0,0,0)
#b
print("+++")
print(vIip+(fNet*dt))
print("+++")
#c
print("+++")
util.posup(posPhone,vIip+fNet,dt)
print("+++")
#d1
tStep=0.02
iPhone15=vpy.sphere(pos=posPhone,radius=.002,make_trail=True)
vpy.sleep(1)
for i in range(60):
    vpy.rate(5)
    tNow=tStep*i
    print(i)
    print(posPhone)
    print(vIip)
    print(pIp)
    print(tNow)
    vIip=util.posup(vIip,fNet,tStep)
    pIp=util.posup(pIp,vIip,tStep)
    iPhone15.pos=pIp
    if i>4:
        iPhone15.trail_color=vpy.color.orange
    if pIp.y>hDennis:
        iPhone15.trail_color=vpy.color.red
    vpy.sleep(1/5)