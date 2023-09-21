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
"""------------------------------------------------------------
------------------------------------------------------------"""

#q4
def gammaV(v,c=util.c()):
    return(1/math.sqrt(1-((vpy.mag(v)/c)**2)))

mPhone=0.2215
hDennis=12.2
vIip=vpy.vec(3.7,2.1,-1.6)
pIp=gammaV(vIip)*mPhone*vIip
fNet=vpy.vec(0,-9.8,0)
dt=0.6
posPhone=vpy.vec(0,0,0)
#b
print("+++")
print(vIip+(fNet*dt))
print("+++")
#c
print("+++")
util.posup(posPhone,vIip+fNet,dt)
print("+++")
#d1
tStep=0.02
iPhone15=vpy.sphere(pos=posPhone,radius=.002,make_trail=True)
vpy.sleep(1)
for i in range(60):
    vpy.rate(5)
    tNow=tStep*i
    print(i)
    print(posPhone)
    print(vIip)
    print(pIp)
    print(tNow)
    vIip=util.posup(vIip,fNet,tStep)
    pIp=util.posup(pIp,vIip,tStep)
    iPhone15.pos=pIp
    if i>4:
        iPhone15.trail_color=vpy.color.orange
    if pIp.y>hDennis:
        iPhone15.trail_color=vpy.color.red
    vpy.sleep(1/5)
        
    
