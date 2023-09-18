# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 10:04:55 2023

@author: Savvie
"""

import vpython as vpy
import vpvecutils as util
import numpy as np 
import math as math


m=2.8*10**11
pos=vpy.vec(4000,9000,0)
vi=vpy.vec(600,32000,0)
fNet=vpy.vec(0,3200,0)

xf=pos+((vi+fNet*21)/2)
x2=util.posup(xf,vi,3600)