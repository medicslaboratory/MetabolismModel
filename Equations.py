import math
import numpy as np


def RHSCunnane(y, p, eat):
    """
    Fonction that defines the equations of the metablism.
    :param y
    """

    # y[0]: Glucose concentration in capillaries
    # y[1]: Ketone concentration in capillaries
    # y[2]: Glucose concentration in neurons
    # y[3]: Lactate concentration in neurons
    # y[4]: Ketone concentration in neurons
    # y[5]: ATP concentration in neurons
    # y[6]: Extracellular glutamate concentration
    # y[7]: Glutamine concentration in astrocytes
    # y[8]: ATP concentration in astrocytes
    # y[9]: Glucose concentration in astrocytes
    # y[10]: Lactate concentration in astrocytes
    # y[11]: Glucose concentration in oligodendrocytes
    # y[12]: Lactate concentration in oligodendrocytes
    # y[13]: ATP concentration in oligodendrocytes

    dydt = np.zeros(15)

    # Glucose in capillaries
    dydt[0] = p.digestGluc * eat.GluSto - p.decayGluBlood * y[0]

    # Ketone in capillaries
    dydt[1] = p.digestKet * eat.KetSto - p.decayKetBlood * y[1]

    # GLUT on the neurons
    GLUTNeu = p.GLUTNeuBase + (p.GLUTNeuMax - p.GLUTNeuBase) * (eat.Insul / p.GLUTInsuHalf) / \
              (1 + (eat.Insul / p.GLUTInsuHalf))
    # Energy (ATP) in neurons form glucose, lactate and Ketone
    EnerNeu = p.EnerGlu * y[2] + p.EnerLac * y[3] + p.EnerKet * y[4]
    # ?? Function for energy in neurons
    fEnerNeu = p.ATPMaxRate * (EnerNeu / p.EnerHalf) / (1 + (EnerNeu / p.EnerHalf))
    # Glucose concentration variation in neurons
    dydt[2] = GLUTNeu * (y[0] / p.GluHalf) / (1 + (y[0] / p.GluHalf)) - fEnerNeu * y[2] / (y[2] + y[3] + y[4])

    # Lactate concentration variation in neurons
    dydt[3] = p.LacOligtoNeuMaxRate * (y[12] / p.LacHalf) / (1 + (y[12] / p.LacHalf)) - fEnerNeu * y[3] / (
                y[2] + y[3] + y[4])

    # Ketone concentration variation in neurons
    dydt[4] = p.KetMaxRate * (y[1] / p.KetHalf) / (1 + (y[1] / p.KetHalf)) - fEnerNeu * y[4] / (y[2] + y[3] + y[4])

    # ATP concentration variation in neurons
    dydt[5] = fEnerNeu - p.ATPdecay * y[5]

    # ?? Function for ATP in neurons
    fATPNeu = 1 / (1 + math.exp(-(y[5] - p.treshATP) / p.tauATP))
    # ?? Function for cognition in neurons
    fCogn = 1 / (1 + math.exp(-(eat.cogn - p.treshCogn) / p.tauCogn))
    # Synaptic activity from neuron
    SynAct = p.SynBase + (p.SynMax - p.SynBase) * fATPNeu * fCogn

    # Extracellular glutamate variation
    dydt[6] = p.SynGlmate * SynAct - p.GlmateAst * y[6] - p.GlmateOlig * y[6]

    # Glutamine concentration variation in astocytes
    dydt[7] = p.GLUTAst * y[6] - p.GlmineDecay * y[7]  # Modif GLUTAst -> GlutAst
    # TODO: p.GLUTAst (ou GLUTAstRate??) ???? Le glutamate ne passe pas par un GLUT...

    # ?? Energy in astrocytes
    EnerAst = p.EnerGlu * y[9] + p.EnerLac * y[10]
    # ?? Function for energy in astrocytes
    fEnerAst = p.ATPMaxRate * (EnerAst / p.EnerHalf) / (1 + (EnerAst / p.EnerHalf))
    # ?? Function for synaptic activity in astrocytes
    fSynAct = 1 / (1 + math.exp(-(SynAct - p.treshSynAct) / p.tauSynAct))
    # ?? Function for glutamine in astrocytes
    fGlmineAst = 1 / (1 + math.exp((y[7] - p.treshGlmineAst) / p.tauGlmineAst))
    # ATP concentration variation in astrocytes
    dydt[8] = fEnerAst * fSynAct * fGlmineAst - y[8] * p.ATPdecay

    # Glucose concentration variation in astrocytes
    dydt[9] = p.GLUTAst * y[0] / (1 + (y[0] / p.GluHalf)) - p.GlmateAstToLac * y[9] - p.GlmateAstToOlig * y[9] - fEnerAst * fSynAct * fGlmineAst * y[9] / (y[9] + y[10])
    # TODO: p.GLUTAst (ou GLUTAstRate??) ???? Pas dans le fichier des paramètres
    #  p.GluHalf ou p.GluHalfAst ??
    #  p.GlmateAstToOlig Ah oui?!?

    # Lactate concentration variation in astrocytes
    dydt[10] = p.GlmateAstToLac * y[9] - p.LacAstToOlig * y[10] - fEnerAst * fSynAct * fGlmineAst * y[10] / (y[9] + y[10])
    # TODO: p.GlmateAstToLac ? Flèche mal placée sur schéma...
    #  p.LacAstToOlig Pas de lactate qui va de astrocyte à olig, plutôt vers neurones...

    # ?? Energy in oligodendrocytes
    EnerOlig = p.EnerGlu * y[11] + p.EnerLac * y[12]
    # ?? Function for energy in oligodendrocytes
    fEnerOlig = p.ATPMaxRate * (EnerOlig / p.EnerHalf) / (1 + (EnerOlig / p.EnerAst))
    # Glucose concentration variation in oligodendrocytes
    dydt[11] = (p.GlmateAstToOlig * y[9] + y[6]) * p.GLUTOlig - fEnerOlig * y[11] / (y[11] + y[12])
    # TODO: p.GLUTOlig (ou GLUTOligRate ?) ???? Pas dans le fichier des paramètres

    # Lactate concentration variation in oligodendrocytes
    dydt[12] = p.LacAstToOlig * y[10] - fEnerOlig * y[12] / (y[11] + y[12])
    # TODO: (même commentaire) p.LacAstToOlig Pas de lactate qui va de astrocyte à olig, plutôt vers neurones...

    # ATP concentration variation in oligodendrocytes
    dydt[13] = fEnerOlig - p.ATPdecay * y[13]

    return dydt
