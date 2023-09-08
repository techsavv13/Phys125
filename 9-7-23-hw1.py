# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 20:42:51 2023

@author: Savvie
"""
from vpython import *
import vpvecutils as util
import numpy as np 

s0 = sphere(pos=vec(0,0,0), radius=0.7, color=color.white)

for i in range(-2,3,4):
    for j in range(-2,3,4):
        for k in range(-2,3,4):
            balls = sphere(pos=vec(i,j,k), radius=0.7, color=color.yellow)
