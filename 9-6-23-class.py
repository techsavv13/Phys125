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
Fg=m*vpy.vec(0,-9.8,0)
dT=4

up=util.posup(vInit,Fg,dT)

i=1

