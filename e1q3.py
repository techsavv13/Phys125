# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 12:27:56 2023

@author: Savvie
"""

import vpython as vpy
import vpvecutils as util
import numpy as np 
import math as math


#q3
posP=vpy.vec(0.0,-1.3,2.6)
vIp=vpy.vec(3600,1200,-2500)
dTp=0.001
#a
upP=util.posup(posP,vIp,dTp)
"""------------------------------------------------------------
------------------------------------------------------------"""
