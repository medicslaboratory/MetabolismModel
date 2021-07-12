
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Import the required modules

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

import Equations as eq
# import parameter as param


# p = param.parameter()

t = np.linspace(0, 30, 100)  # 100 pts equidistant between 0 and 30.

y0 = np.zeros(16)  # the initial conditions
y0[0] = 4     # Glucose concentration in capillaries (normal range about 4 to 5 mM)
y0[1] = 0.3  # Ketone concentration in capillaries (Pan, 2001 : 2.12 en mM) (Fortier, 2019) en mM
y0[2] = 2     # Glucose concentration in neurons (Qutub, 2005) en 1–2 mM (pour brain)
y0[3] = 0.70  # Lactate concentration in neurons (Pan, 2001: 0.70 en mM)...louche
y0[4] = 0.24  # Ketone concentration in neurons (Pan, 2001) en mM
y0[5] = 2     # ATP concentration in neurons (Trevisiol,2017) en mM
y0[6] = 0.001  # Extracellular glutamate concentration (Herman, 2011 : ∼25 nM to up to ∼30 µM) en mM (0.001 mM = 1µM)
y0[7] = 1     # Glutamine concentration in astrocytes (Yudkoff, 1998) mM
y0[8] = 1.5   # Glucose concentration in astrocytes (Qutub, 2005) en 1–2 mM (pour brain)
y0[9] = 0.07  # Pyruvate concentration in astrocytes (rapport env. 1:10 avec lactate)
y0[10] = 0.70  # Lactate concentration in astrocytes (Pan, 2001: 0.70 en mM)...louche
y0[11] = 2    # ATP concentration in astrocytes (Lerchundi,2020) en mM
y0[12] = 1.5  # Glucose concentration in oligodendrocytes (Qutub, 2005) en 1–2 mM (pour brain)
y0[13] = 0.07  # Pyruvate concentration in oligodendrocytes (rapport env. 1:10 avec lactate)
y0[14] = 0.70  # Lactate concentration in oligodendrocytes (Pan, 2001: 0.70 en mM)...louche
y0[15] = 2    # ATP concentration in oligodendrocytes ...suppose que comme Astrocyte et Neurone en mM

ys = odeint(eq.RHSCunnane, y0, t)
# ys = np.array(ys).flatten()

plt.plot(t, ys[:, 2], label='GluNeu(t)')
plt.plot(t, ys[:, 1], label='KetNeu(t)')
plt.plot(t, ys[:, 5], label='ATPNeu(t)')
plt.plot(t, ys[:, 6], label='ExtGlutamate(t)')
plt.plot(t, ys[:, 7], label='GlutamineAst(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()