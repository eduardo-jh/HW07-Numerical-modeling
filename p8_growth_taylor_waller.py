#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BE523 Biosystems Analysis & Design
HW7 - Problem 8. Growth with exponential equation and Euler method
Professor Waller solution

Created on Tue Feb 23 00:34:17 2021
@author: eduardo
"""
import math
import numpy as np
import matplotlib.pyplot as plt

C_initial = 1
mu = 0.1
time_step = 2
num_time_step = 5

time = np.zeros(num_time_step+1)
C = np.zeros(num_time_step+1)
Cexp = np.zeros(num_time_step+1)
C_taylor = np.zeros(num_time_step+1)
C[0] = C_initial
Cexp[0] = C_initial
C_taylor[0] =  C_initial

for i in range(1, num_time_step+1):
    time[i] = i*time_step
    dc = mu*time_step*C[i-1]
    C[i] = C[i-1] + dc
    Cexp[i] = Cexp[i-1]*math.exp(mu*time_step)

for i in range(1, num_time_step+1):
    C_taylor[i] = C_taylor[i-1] + mu*C_taylor[i-1]*time_step + (mu**2)*C_taylor[i-1]*((time_step**2)/2)

error2 = (mu**2)*2*(2**2)/2
error5 = (mu**2)*2*(5**2)/2
print('error2=', error2, 'error5=', error5)

plt.figure(0)
plt.plot(time, C, 'rx', time, Cexp, 'b+', time, C_taylor, 'g-')
plt.legend(['Euler', 'Exponential', 'Taylor expansion'], loc='best')