#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on Tue Feb  2 17:49:01 2021
@author: eduardo
"""
import numpy as np
import matplotlib.pyplot as plt

C_initial = 1
mu = 0.1

time_step = 1
initial_time_step = 0
num_time_steps = 10

C = np.ones(num_time_steps + 1)
C = C * C_initial
time = np.zeros(num_time_steps + 1)

for i in range(1, num_time_steps+1):
    time[i] = initial_time_step + i*time_step
    dc = mu*time_step*C[i-1]
    C[i] = C[i-1] + dc
    
plt.figure(0)
plt.plot(time, C)
plt.xlabel('Day')
plt.ylabel('AFDW g/L')