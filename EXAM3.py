# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 21:04:57 2023

@author: Savvie
"""

from vpython import *

def eChrg():return(1.6*10**-19)

def fallgraph(r_now,m,v,dt,tnow,tmax,tstep):
# Initial information for a ball tossed in the air. 
# No air resistance. On the Earth.
#old code from 9/7 for falling objects
    #r_now = vec(0,0,0) # m
    print('r_now',r_now)
    #m = 0.1 # kg
    #v = vec(3,3,0) # m/s
    #dt = 0.1 #s

    p_now = m*v
    
    # Calculate forces
    Fg = m * vec(0,-9.8,0)
    F_net = Fg
    print('F_net',F_net)
    # update momentum
    p_future = p_now + F_net * dt
    # update position (including v_avg)
    v_avg = p_future/m
    r_future = r_now + v_avg*dt
    print('r_future',r_future)
    
    ball = sphere(pos=r_now, radius = 0.001, make_trail=True)
    
                
    i = 1
    while i < 100:
      rate(500)
      # Calculate forces
      print('i',i)
      Fg = m * vec(0,-9.8,0)
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
      i=i+1
      sleep(.1)
     


#q1
echrg=eChrg()
mhe3 = 5.0082*10**-27#kg
mhe4 = 6.6447*10**-27#kg
mpro = 1.6726*10**-27#kg
touchies=1.73*10**-15#m

startm = mhe3*2
endm = mhe4+2*mpro
dm=startm-endm

print(echrg*2)
print(startm)
print(endm)
print(dm)



print("\n----------------------------\n")
#q2
mball=.32#kg
dsp=0.06#m
Ks=350#N/m

us=.5*Ks*(dsp**2)
print(us)

vi=mball*us
print(vi)

#fallgraph(vec(0,0.06,0),mball,vec(0,vi,0),0.001,1,10,1)

print("\n----------------------------\n")

#q3

m=0.038
r=6.7
ft=0.2
dyo=0.52

mi=.5*m*(r**2)
print(mi,"\n")

fg=9.8*m
print(fg)
fnet=fg-ft
print(fnet,"\n")

krot=.5*mi*(dyo**2)
print(krot)


