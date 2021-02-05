#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BE523 Biosystems Analysis & Design
HW7 - Problem 8. Growth with exponential equation and Euler method

Created on Tue Feb  2 16:49:36 2021
@author: eduardo
"""
import numpy as np
import matplotlib.pyplot as plt

C_0 = 1  # initial concentration
dt = 2  # time interval, days
mu = 0.1
steps = 10

t = np.array(range(0, steps+1, dt)) # time vector @ 'dt' steps
CEuler = np.zeros(len(t))
CTaylor = np.zeros(len(t))

# Making predictions of concentration using numerical method (Euler)
CEuler[0] = C_0
CTaylor[0] = C_0
for i in range(1, len(t)):
    CEuler[i] = CEuler[i-1] + (CEuler[i-1]*mu*dt) #  Euler
    CTaylor[i] = CTaylor[i-1] + (CTaylor[i-1]*mu*dt) + (pow(mu, 2) * CTaylor[i-1] * pow(dt, 2)/2)

# Making predictions using the analytical solution (exponential equation)
Cexp = C_0 * np.exp(mu*t)

plt.figure(1)
plt.plot(t, Cexp, 'b-', t, CEuler, 'rx', t, CTaylor, 'k+')
plt.legend([r'Analytic $C=C_0\cdot \exp (\mu \times t)$ $\mu=$%0.1f dt=%d' % (mu, dt) ,
            r'Euler $C=C_{i-1}+(C_{i-1}\cdot\mu\cdot dt)$',
            r'Taylor series (3 terms)'],
            # r'Taylor $C=C_{i-1}+(C_{i-1}\cdot\mu\cdot dt)+(\mu^2\cdot C_{i-1}(dt^2/2))$'],
           loc='best')
plt.xlabel('Time (days)')
plt.ylabel('Concentration (mg/L)')
plt.savefig('p8_euler_dt=%d_mu=%.1f.png' % (dt, mu), dpi=300, bbox_inches='tight')
plt.show()
