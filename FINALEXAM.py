# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 10:54:49 2023

@author: Savvie
"""
import vpython as vpy

#A.1
'''
soccerball = vpy.sphere(pos=vpy.vec(6,0,2),radius=0.23,
                            make_trail=True)
mball=0.45#kg
i=0
dt=0.2
p_now=mball*vpy.vec(-12,13,4)
print('p_now',p_now)
r_now=soccerball.pos
while i < 10:
   vpy.rate(500)
   # Calculate forces
   print('i ',i)
   Fg = mball * vpy.vec(0,-9.8,0)
   F_net = Fg
   print('F_net',F_net)
   # update momentum
   p_future = p_now + F_net * dt
   # update position (including v_avg)
   v_avg = p_future/mball
   r_future = r_now + v_avg*dt
   print('r_future',r_future)
       
   r_now = r_future
   p_now = p_future
   print('p_now',p_now)
   soccerball.pos = r_now
   i+=1
   vpy.sleep(.1)


"""
-----------------------------------------------
"""
#B.2

# Constants
G = 6.7e-11
rEarth = vpy.vec(-4e10,1.44e11,-1.2e11) # position of Earth
mEarth = 6e24  # mass of Earth
rSun = vpy.vec(1.2e8,6e10,0)
mSun = 2e30 # mass of spacecraft

# find r
rS=rSun-rEarth#r for f(earth on sun)
rE=rEarth-rSun#r for f(sun on earth)
# print it out to check
#print(r)
# continue along, and find the force.
fgrabS=-G*((mEarth*mSun)/vpy.mag(rS)**2)*vpy.hat(rS)
fgrabE=-G*((mEarth*mSun)/vpy.mag(rE)**2)*vpy.hat(rE)
fgrabS2=-G*((mEarth*mSun)/vpy.mag(rS*2)**2)*vpy.hat(rS*2)
print("force from earth on sun\n vec ",fgrabS," mag ",vpy.mag(fgrabS))
print("force from sun on earth\n vec ",fgrabE," mag ",vpy.mag(fgrabE))
print(fgrabS+fgrabE)
print("f for double the distance ",vpy.mag(fgrabS2))
'''
"""
-----------------------------------------------
"""
#D.1

mp=0.25
vp1=0
vp2=0.6

kei1=.5*mp*vp1**2
kei2=.5*mp*vp2**2
print(kei1)
print(kei2)


kef1=.5*mp*0.6**2
print(kef1)
print(kef1-kei2)

