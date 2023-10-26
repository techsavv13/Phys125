# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 10:28:49 2023

@author: Savvie
"""

from vpython import *
import vpvecutils as util
import numpy as np 
import math as math
"""

#q1
G = 6.7e-11
ma1=4.5e9#kg
ra1=vec(-0.6,0.2,0.032)#km
ma2=3.2e12#kg
ra2=vec(0.24,-0.19,8.2)#km

r21=ra2-ra1
r12=ra1-ra2
print("r2-r1=",r21)
print("r1-r2=",r12)

fgrab2x1=-G*((ma1*ma2)/mag(r21)**2)*hat(r21)
fgrab1x2=-G*((ma1*ma2)/mag(r12)**2)*hat(r12)
print("fgrab2x1 (vec) \n   ",fgrab2x1)
print("fgrab1x2 (vec) \n   ",fgrab1x2)
print("fgrab2x1 (mag) \n   ",mag(fgrab2x1))
print("fgrab1x2 (mag) \n   ",mag(fgrab1x2))

ma3=3.7e12#kg
ra3=vec(3,0.2,-0.65)#km

r31=ra3-ra1
print("r3-r1=",r31)

fgrab3x1=-G*((ma1*ma3)/mag(r31)**2)*hat(r31)
fnetast=fgrab3x1+fgrab2x1
print("fgrab3x1 (vec) \n   ",fgrab3x1)
print("fgrab3x1 (mag) \n   ",mag(fgrab3x1))
print("fnet1 (vec) \n   ",fnetast)
print("fnet1 (mag) \n   ",mag(fnetast))
"""


#q3
uk=0.9
v=2.5#m/s
m=77.5#kg
fg=9.8#m/s^2

fFri=uk*v*m*fg
print(fFri)



