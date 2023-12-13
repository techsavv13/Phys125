# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 10:54:49 2023

@author: Savvie
"""
import vpython as vpy

#a.1

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