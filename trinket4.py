# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 11:56:07 2023

@author: Savvie
"""
from vpython import *
import vpvecutils as util
import numpy as np 
import math as math



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
v0 = vec(0,0,0)
pCraft = mCraft * v0

dt = 2
t = 0

# move camera to give a better view
scene.center = vec(2*REarth, 0, 0)  
# don't let camera zoom out automatically (you can still do it manually)
scene.autoscale = False  

# find r
r=Craft.pos-Earth.pos
# print it out to check
print(r)
# continue along, and find the force.
fgrab=-G*((mEarth*mCraft)/mag(r)**2)*hat(r)
print(fgrab)


while t < 1e7:
  rate(500)
  r=Craft.pos-Earth.pos
  fgrab=-G*((mEarth*mCraft)/mag(r)**2)*hat(r)
  pCraft = fgrab*dt
  Craft.pos+=pCraft*dt
  print(fgrab.x)
  if mag(r)<=REarth:   
     print("ablative lithobraking manuver executed") 
     break
  t+=dt
