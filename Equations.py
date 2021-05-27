
import math
import numpy as np
import parameters as param


def RHSCunnane(y, t):
    """
    Fonction that defines the equations of the metablism.
    :param y
    """

    # y[0]: Glucose concentration in capillaries (normal range about 4 to 5 mM)
    # y[1]: Ketone concentration in capillaries
    # y[2]: Glucose concentration in neurons
    # y[3]: Lactate concentration in neurons
    # y[4]: Ketone concentration in neurons
    # y[5]: ATP concentration in neurons

    # y[6]: Extracellular glutamate concentration
    # y[7]: Glutamine concentration in astrocytes

    # y[8]: Glucose concentration in astrocytes
    # y[9]: Pyruvate concentration in astrocytes
    # y[10]: Lactate concentration in astrocytes
    # y[11]: ATP concentration in astrocytes

    # y[12]: Glucose concentration in oligodendrocytes
    # y[13]: Pyruvate concentration in oligodendrocytes
    # y[14]: Lactate concentration in oligodendrocytes
    # y[15]: ATP concentration in oligodendrocytes

    p = param.parameter()

    dydt = np.zeros(16)