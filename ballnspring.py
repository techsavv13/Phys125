# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 21:09:42 2023

@author: Savvie
"""

from vpython import *

m = 75 #kg
stretch = 0.3e-2 #m
density_gcm = 4 # g/cm^3
m_mol = 23e-3 #kg
d_wire = 0.2e-2 # m
r_wire = d_wire/2
l_wire = 2 #m
# 1kg / 1000g * (100cm/m)^3
density = density_gcm * (1/1000)*(100)**3
print('density',density, 'kg/m^3')
g = 9.8
k_wire = m*g/stretch
print(k_wire, 'N/m')
m_atom = m_mol/6.022e23
d = (m_atom/density)**(1/3)
print(d, 'm')
Nchains = pi*r_wire**2 / d**2
print('Nchains',Nchains)
Nbonds = l_wire/d
print('Nbonds',Nbonds)
ksi = k_wire * Nbonds / Nchains
print('ksi',ksi,'N/m')