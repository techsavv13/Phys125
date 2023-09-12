# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:11:59 2023

@author: Savvie
"""

from vpython import *
import vpvecutils as util
import numpy as np 

tracc=box(pos=vec(0,1,0),axis=vec(1,0,0),length=2,width=.25,height=.125)

g=util.grav()
m=.8
tStep=0.01

Cpos=vec(0,.125,0)
vi=vec(.5,0,0)

cart=box(pos=Cpos,length=.1,width=.27,height=.125,color=color.purple)

#while Cpos.x()<2:
    
