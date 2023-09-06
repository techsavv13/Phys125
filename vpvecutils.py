# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 15:20:48 2023

@author: Savvie
A set of vPython vector utilities of my own creation
"""
import vpython as vpy


def getvec(varname):
    vin = vpy.vec(input("gibs "+varname+" x "),input("gibs "+varname+" y "),input("gibs "+varname+" z "))
    print(varname+" "+str(vin))
    return vin

def posup(ri=-0,vavg=-0,dt=-0):
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

def momentum(fnet=-0,dt=-0):
    if fnet == -0:
        fnet = getvec("fnet")
    if dt == -0:
        dt = float(input("needs dt "))
        print("dt "+ str(dt))
    dp = fnet*dt
    print(dp)
    return dp

