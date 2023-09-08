# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 08:27:15 2023

@author: Savvie
A series of common simulations and visualisations
"""
import vpython as vpy
import vpvecutils as util
import numpy as np 


def fallgraph(r_now,m,v,dt,tnow,tmax,tstep):
    # Initial information for a ball tossed in the air. 
    # No air resistance. On the Earth.
 
    print('r_now',r_now)

    p_now = m*v
    
    # Calculate forces
    Fg = m * vpy.vec(0,-9.8,0)
    F_net = Fg
    print('F_net',F_net)
    # update momentum
    p_future = p_now + F_net * dt
    # update position (including v_avg)
    v_avg = p_future/m
    r_future = r_now + v_avg*dt
    print('r_future',r_future)
    
    ball = vpy.sphere(pos=r_now, radius = 0.01, make_trail=True)
    
                
    i = tnow
    while i < tmax:
      vpy.rate(5)
      # Calculate forces
      Fg = m * vpy.vec(0,-9.8,0)
      F_net = Fg
      print('F_net',F_net)
      # update momentum
      p_future = p_now + F_net * dt
      # update position (including v_avg)
      v_avg = p_future/m
      r_future = r_now + v_avg*dt
      print('r_future',r_future)
          
      r_now = r_future
      p_now = p_future
      ball.pos = r_now
      i+=tstep
      
      
fallgraph(vpy.vec(0,0,0),0.1,vpy.vec(3,3,0),0.1,1,10,1)