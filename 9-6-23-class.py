# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 10:09:39 2023

@author: Savvie
"""
#default imports
import vpython as vpy
import vpvecutils as util
import numpy as np 

#definitions
m=0.1#kg
vInit=vpy.vec(3,3,0)
pnow=m*vInit
rnow=vpy.vec(0,0,0)
Fg=m*util.grav()
dT=4

up=util.posup(vInit,Fg,dT)

i=1


ball=vpy.sphere(pos=rnow)
while i<=10:
    #calc force
    fnet=Fg
    #posup momentum
    util.posup()
    #posup pos
    #p=m*v
    #v=p/m
    
    
    i+=1