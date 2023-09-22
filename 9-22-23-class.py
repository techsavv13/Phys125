# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 10:12:20 2023

@author: Savvie
"""

import vpython as vpy
import vpvecutils as util
import numpy as np 
import math as math

qe=1.6*10**-19
q1=2*qe
q2=3*qe
r1=vpy.vec(0,-2,1)
r2=vpy.vec(5,3,7)
r=r2-r1


f=(util.oofpez()*q1*q2/vpy.mag(r)**2)*vpy.hat(r)
print(f)