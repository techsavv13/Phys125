# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 12:27:19 2023

@author: Savvie
"""

import vpython as vpy
import vpvecutils as util
import numpy as np 
import math as math


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
