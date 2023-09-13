# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:11:59 2023

@author: Savvie
"""

from vpython import *
import vpvecutils as util
import numpy as np 
import math as math

tracc=box(pos=vec(1,0,0),axis=vec(5,0,0),
          length=2,width=.25,height=.125,color=color.gray(0.25))

g=util.grav()
m=.8
le=.1
tStep=0.01


Cpos=vec(.05,.125,0)
vi=vec(.5,0,0)

cart=box(pos=Cpos,length=le,width=.27,height=.125,color=color.purple)

while 1==1:
    rate(100)
    posP=vi*tStep
    Cpos+=posP
    cart.pos=Cpos
    if math.isclose(Cpos.x,1.95):break

sleep(1.5)
Cpos=vec(.05,.125,0)
dv=vec(-.05,0,0)
while 1==1:
    rate(100)
    vi=vi+dv*tStep
    posP=vi*tStep
    Cpos+=posP
    cart.pos=Cpos
    if Cpos.x<0:break

sleep(3)
cart.visible=False
