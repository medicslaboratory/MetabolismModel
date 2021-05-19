import math
import numpy as np


def RHSCunnane(y, p):
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


    dydt = np.zeros(16)

    # Glucose in capillaries
    dydt[0] = p.digestGlu * p.eatGluSto - p.decayGluBlood * y[0]

    # Ketone in capillaries
    dydt[1] = p.digestKet * p.eatKetSto - p.decayKetBlood * y[1]

    # GLUT in the neurons
    # GLUTNeu = p.GLUTNeuBase + (p.GLUTNeuMax - p.GLUTNeuBase) * (p.eatInsul / p.GLUTInsuHalf) / (1 + (p.eatInsul / p.GLUTInsuHalf))
    # ToDo : Revoir si ok... (suppose que tout pareil)
    GLUT = p.GLUTBase + (p.GLUTMax - p.GLUTBase) * (p.eatInsu / p.GLUTInsuHalf) / (1 + (p.eatInsu / p.GLUTInsuHalf))
    GLUTNeu = GLUT

    # Glucose concentration variation in neurons
    # TODO : Ajout entrée de Glucose des Astrocytes (s'il y a lieu)
    fGluNeuToAcCoA = p.VGluMaxNeu * (y[2] / p.KGluHalfNeu) / (1 + (y[2] / p.KGluHalfNeu))
    dydt[2] = GLUTNeu * (y[0] / p.GluHalfNeu) / (1 + (y[0] / p.GluHalfNeu)) - fGluNeuToAcCoA

    # Lactate concentration variation in neurons
    # TODO : Revoir entrée de Lactate des Astrocytes
    fLacNeuToAcCoA = p.VLacMaxNeu * (y[2] / p.KLacHalfNeu) / (1 + (y[2] / p.KLacHalfNeu))
    dydt[3] = p.LacOligToNeuMaxRate * (y[14] / p.LacHalf) / (1 + (y[14] / p.LacHalf)) + p.LacAstToNeu * y[10] - fLacNeuToAcCoA

    # Ketone concentration variation in neurons
    fKetNeuToAcCoA = p.VKetMaxNeu * (y[2] / p.KKetHalfNeu) / (1 + (y[2] / p.KKetHalfNeu))
    dydt[4] = p.KetMaxRate * (y[1] / p.KetHalf) / (1 + (y[1] / p.KetHalf)) - fKetNeuToAcCoA

    # Acetyl-CoA par Glu + par Lac + par Ket
    AcetylCoANeu = fGluNeuToAcCoA + fLacNeuToAcCoA + fKetNeuToAcCoA

    fAcetylCoANeu = p.AceCoAMaxRateNeu * (AcetylCoANeu / p.ACoAHalfNeu) / (1 + (AcetylCoANeu / p.ACoAHalfNeu))

    # TODO: Revoir ATP: Ajout 2 ATP (pour Glu -> pyruvate) + 1 ATP (Acetyl-CoA dans TCA)
    # Function for ATP in neurons
    fATPNeu = 1 / (1 + math.exp((y[5] - p.treshATP) / p.tauATP))
    # ATP concentration variation in neurons
    dydt[5] = fATPNeu * fAcetylCoANeu - p.ATPdecay * y[5]

    # dATP / dt = -cATP + f(ATP, AcetylCoa)
    # f(ATP, AcetylCoa) = f_1(ATP) * f_2(AcetylCoa)
    # f_2(x) = vmax(x / xhalf)(1 + (x / xhalf))
    # f_1(ATP) = 1 / (1 + exp((ATP - ATPtresh) / ATPslope))

    # sigma(x)=1/(1+exp(-x))
    # sigma'=sigma(1-sigma)

    # Function for cognition in neurons
    fCogn = 1 / (1 + math.exp(-(p.eatCogn - p.treshCogn) / p.tauCogn))
    # Synaptic activity from neuron
    SynAct = p.SynBase + (p.SynMax - p.SynBase) * fATPNeu * fCogn

    # __________________

    # Extracellular glutamate variation
    dydt[6] = p.SynGlmate * SynAct - p.GlmateAst * y[6] - p.GlmateOlig * y[6]

    # Glutamine concentration variation in astrocytes
    dydt[7] = p.GlmateAst * y[6] * p.GlmateToGlmineAst - p.GlmineDecay * y[7] - p.GlmineToATP * y[7] - p.GlmineToNeu * y[7]


    # y[8]: Glucose concentration in astrocytes
    # y[9]: Pyruvate concentration in astrocytes
    # y[10]: Lactate concentration in astrocytes
    # y[11]: ATP concentration in astrocytes

    fGluToPyrAst = p.VGluMaxAst * (y[8] / p.KGluHalfAst) / (1 + (y[8] / p.KGluHalfAst))
    # Glucose concentration variation in astrocytes
    # TODO : Ajout sortie de Glucose vers neurone (s'il y a lieu)
    dydt[8] = GLUT * (y[0] / p.GluHalfAst) / (1 + (y[0] / p.GluHalfAst)) - p.GluAstToOlig * y[8] - fGluToPyrAst

    # Pyruvate to lactate
    fPyrToLacAst = p.VPyrMaxAst * (y[9] / p.KPyrHalfAst) / (1 + (y[9] / p.KPyrHalfAst))
    # Pyruvate to ATP
    fPyrToATPAst = p.PyrATPMaxRateAst * (y[9] / p.PyrATPHalfAst) / (1 + (y[9] / p.PyrATPHalfAst))
    # Pyruvate par Glu - to Lac - to ATP
    PyrAst = fGluToPyrAst - fPyrToLacAst - fPyrToATPAst
    # Pyruvate concentration variation in astrocytes
    dydt[9] = p.PyrMaxRateAst * (PyrAst / p.PyrHalfAst) / (1 + (PyrAst / p.PyrHalfAst))

    # Lactate concentration variation in astrocytes
    # TODO : Revoir sortie de Lactate vers neurone
    dydt[10] = fPyrToLacAst - p.LacAstToOlig * y[10] - p.LacAstToNeu * y[10]

    # TODO: Revoir ATP: Ajout 2 ATP (pour Glu -> pyruvate) + 1 ATP (dans TCA) - 2 ATP (glutamate -> glutamine)
    #  Revoir ATP créé par Glutamine (p.ATPfromGlmine *)
    # Function for ATP in astrocytes (pas sur que bonne fonction...)
    fATPAst = 1 / (1 + math.exp(-(y[11] - p.treshATPAst) / p.tauATPAst))
    # ATP concentration variation in neurons
    dydt[11] = fATPAst * fPyrToATPAst + p.GlmineToATP * y[7] - p.ATPdecay * y[11]


    # y[12]: Glucose concentration in oligodendrocytes
    # y[13]: Pyruvate concentration in oligodendrocytes
    # y[14]: Lactate concentration in oligodendrocytes
    # y[15]: ATP concentration in oligodendrocytes

    fGluToPyrOlig = p.VGluMaxOlig * (y[11] / p.KGluHalfOlig) / (1 + (y[11] / p.KGluHalfOlig))
    # Glucose concentration variation in oligodendrocytes
    # TODO: Revoir impact glutamate on GLUT ...
    dydt[11] = GLUT * p.GluAstToOlig * y[8] + (y[0] / p.GluHalfOlig) / (1 + (y[0] / p.GluHalfOlig)) * GLUT * p.GlmateGLUT * p.GlmateOlig * y[6] - fGluToPyrOlig

    # Pyruvate to lactate
    fPyrToLacOlig = p.VPyrMaxOlig * (y[9] / p.KPyrHalfOlig) / (1 + (y[9] / p.KPyrHalfOlig))
    # Pyruvate to ATP
    fPyrToATPOlig = p.PyrATPMaxRateOlig * (y[9] / p.PyrATPHalfOlig) / (1 + (y[9] / p.PyrATPHalfOlig))
    # Pyruvate par Glu - to Lac - to ATP
    PyrOlig = fGluToPyrOlig - fPyrToLacOlig - fPyrToATPOlig
    # Pyruvate concentration variation in oligodendrocytes
    dydt[13] = p.PyrMaxRateOlig * (PyrOlig / p.PyrHalfOlig) / (1 + (PyrOlig / p.PyrHalfOlig))

    # Lactate concentration variation in oligodendrocytes
    dydt[14] = p.LacAstToOlig * y[10] + fPyrToLacOlig - p.LacOligToNeuMaxRate * (y[14] / p.LacHalf) / (1 + (y[14] / p.LacHalf))

    # TODO: Revoir ATP : Ajout 2 ATP (pour Glu -> pyruvate) + 1 ATP (dans TCA)
    # Function for ATP in oligodendrocytes
    fATPOlig = 1 / (1 + math.exp(-(y[15] - p.treshATPOlig) / p.tauATPOlig))
    # ATP concentration variation in oligodendrocytes
    dydt[15] = fATPOlig * fPyrToATPOlig - p.ATPdecay * y[15]

    return dydt
