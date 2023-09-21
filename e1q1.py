# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 12:26:25 2023

@author: Savvie
"""

import vpython as vpy
import vpvecutils as util
import numpy as np 
import math as math

#q1
A=vpy.vec(6,3,-2)
B=vpy.vec(-4,0,4)
#a
mgA=vpy.mag(A)#used var viewer in IDE
#b
hatA=vpy.hat(A)
print(hatA)
#c
c=A+B
print(c)
#d
d=A-B
print(d)
"""------------------------------------------------------------
------------------------------------------------------------"""
