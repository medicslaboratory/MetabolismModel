# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Import the required modules

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

import Equations as eq
import parameter as param


p = param.parameter()

t = np.linspace(0,5,100)
y0 = 1.0  # the initial condition
ys = odeint(eq.RHSCunnane(y,p,eat), y0, t)
ys = np.array(ys).flatten()


