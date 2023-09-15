# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 10:15:12 2023

@author: Savvie
"""

from vpython import *
import vpvecutils as util
import numpy as np 
import math as math


star=vec(1.5*10**11,.5*10**11,0)
planI=vec(2*10**11,1.5*10**11,0)

s2p=star-planI
print(s2p)
shat=hat(s2p)
G=6.7e-11
m1=1e30
m2=5e24
fmag=G*m1*m2/shat**2
print(fmag)