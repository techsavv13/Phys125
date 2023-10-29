# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 11:56:07 2023

@author: Savvie
"""
from vpython import *

# Constants
G = 6.7e-11
REarth = 6.4e6 # radius of Earth
mEarth = 6e24  # mass of Earth
mCraft = 175 # mass of spacecraft

# Objects and initial values
Earth = sphere(pos=vec(0,0,0), radius = REarth, m = mEarth, color=color.cyan)
Craft =  sphere(pos=Earth.pos + vec(4*REarth, 0, 0), color=color.magenta,  
          make_trail = True,
          m = mCraft,
          radius  = REarth/12 )

v0 = vec(input("need x   "),input("need y   "),input("need z   "))
pCraft = mCraft * v0
vcr=pCraft/mCraft

print(v0)

dt = 2
t = 0
fgr=graph(xtitle="t",ytitle="force",align='left',width=400,height=250)
fgraph=gcurve(color=color.red,graph=fgr)

vgr=graph(xtitle="t",ytitle="velocity",align='left',width=400,height=250)
vxgraph=gcurve(color=color.red,graph=vgr)
vygraph=gcurve(color=color.blue,graph=vgr)
vzgraph=gcurve(color=color.green,graph=vgr)

pgr=graph(xtitle="t",ytitle="pos",align='left',width=400,height=250)
xgraph=gcurve(color=color.red,graph=pgr)
ygraph=gcurve(color=color.blue,graph=pgr)
zgraph=gcurve(color=color.green,graph=pgr)

# move camera to give a better view
scene.center = vec(2*REarth, 0, 0)  
# don't let camera zoom out automatically (you can still do it manually)
scene.autoscale = False  

# find r
r=Craft.pos-Earth.pos
# print it out to check
#print(r)
# continue along, and find the force.
fgrab=-G*((mEarth*mCraft)/mag(r)**2)*hat(r)
#print(fgrab)

limitt=float(input("how long?   "))
print(limitt," cycles")

ctn=input("continue y/n    ")

if ctn=="y":
    while t < limitt:
      rate(500)
      r=Craft.pos-Earth.pos
      fgrab=-G*((mEarth*mCraft)/mag(r)**2)*hat(r)
      pCraft += fgrab*dt
      Craft.pos+=pCraft*dt
      vcr=pCraft/mCraft
      #print(fgrab.x)
      xgraph.plot(t,Craft.pos.x)
      ygraph.plot(t,Craft.pos.y)
      zgraph.plot(t,Craft.pos.z)
      fgraph.plot(t,mag(fgrab))
      vxgraph.plot(t,vcr.x)
      vygraph.plot(t,vcr.y)
      vzgraph.plot(t,vcr.z)
      if mag(r)<=REarth:   
         print("ablative lithobraking manuver executed") 
         break
      t+=dt
    print("Done")
elif ctn == "n":print("execution terminated")
else:print("unconventonal\ni like it")