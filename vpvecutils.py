# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 15:20:48 2023

@author: Savvie
A set of vPython vector utilities of my own creation
"""
import vpython as vpy

#literally just gravity
def grav():return(vpy.vec(0,-9.8,0))

#speedo lite
def c():return(3*10**8)

#1hr in seconds
def hr():return(3600)

#oofpez
def oofpez():return(9*10**9)

#electron mass
def mE():return(9*10**-31)

#electron charge
def eChrg():return(1.6*10**-19)

#console vector imports
def getvec(varname):
    vin = vpy.vec(input("gibs "+varname+" x "),input("gibs "+varname+" y "),input("gibs "+varname+" z "))
    print(varname+" "+str(vin))
    return vin

#position updoot formula
def posup(ri=-0,vavg=-0,dt=-0,ball=-0):
    if ri == -0:
        ri = getvec("ri")
    if vavg == -0:
        vavg = getvec("vavg")
    if dt == -0:
        dt = float(input("needs dt "))
        print("dt "+ str(dt))
    rf = ri+vavg*dt
    print(rf)
    return rf

#momentum gubbin
def momentum(fnet=-0,dt=-0):
    if fnet == -0:
        fnet = getvec("fnet")
    if dt == -0:
        dt = float(input("needs dt "))
        print("dt "+ str(dt))
    dp = fnet*dt
    print(dp)
    return dp

