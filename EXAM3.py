# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 21:04:57 2023

@author: Savvie
"""

from vpython import *


#q1
mhe3 = 5.0082*e**-27
mhe4 = 6.6447*e**-27
mpro = 1.6726*e**-27
touchies=1.73*e**-15

startm = mhe3*2
endm = mhe4+2*mpro
dm=startm-endm

print(startm)
print(endm)
print(dm)