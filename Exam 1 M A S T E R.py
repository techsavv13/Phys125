# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 09:24:19 2023

@author: Savvie

EXAM 1

SPLIT PROBLEMS OUT
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

#q2
c=util.c()
mE=util.mE()
vI=c*.96
def gamma(v,c=util.c()):
    return(1/math.sqrt(1-((v/c)**2)))
#a
p=gamma(vI)*mE*vI
print(p)
#b
print(gamma(40))#so small as to be irrelivant
mSlo=p/40
print(mSlo)
checkMe=gamma(40)*mSlo*40
print(math.isclose(p,checkMe))
#c
qantE=mSlo/mE
print(qantE)
print(1*10**7)#figuring out exponent for scinote, thank the gods for monospace font
"""------------------------------------------------------------
------------------------------------------------------------"""

#q3
posP=vpy.vec(0.0,-1.3,2.6)
vIp=vpy.vec(3600,1200,-2500)
dTp=0.001
#a
upP=util.posup(posP,vIp,dTp)
#b





