class parameter():
    """
    Class defining the parameters of the model.
    """

    def __init__(self):
        # Parameters for digestion and metabolism in blood
        self.digestKet = 0.01  # (1/min) Speed at which ketones go from stomach to blood
        self.digestGluc = 0.01  # (1/min) Speed at which glucose go from stomach to blood
        self.decayGluBlood = 0.01  # (1/min) Speed at which glucose disappear from blood (not going to neural cells)
        self.decayKetBlood = 0.01  # (1/min) Speed at which ketones disappear from blood (not going to neural cells)

        # Parameters for GLUT transporters
        self.GLUTNeuBase = 0.1  # (mole/min) Base activity of GLUT transporters activity in neurons
        self.GLUTNeuMax = 0.5  # (mole/min) Maximal activity of GLUT transporters activity in neurons
        self.GLUTInsuHalf = 1  # (g/ml) Insulin concentration at which GLUT transporters are half activated
        self.GLUTAstRate = 0.5  # (1/min) Activity of GLUT transporters in astrocytes
        self.GLUTOligRate = 0.5  # (1/min) Activity of GLUT transporters in astrocytes

        # Parameters for quantities in neurons
        self.GluHalf = 0.5  # (g/ml) Concentration of capillary glucose at which glucose transport by GLUT into
                            # neurons is half maximal
        self.EnerGlu = 1  # (?)  Energy of glucose that will allow to create ATP
        self.EnerLac = 1  # (?)  Energy of lactate that will allow to create ATP
        self.EnerKet = 1  # (?)  Energy of ketone that will allow to create ATP   %AJOUT MOI
        self.ATPMaxRate = 1  # (g /(ml min)?)  Maximal rate of ATP creation
        self.EnerHalf = 1  # (g/ml ?) Available energy concentration at which ATP creation is half maximal

        self.LacOligtoNeuMaxRate = 1  # (g/min) Maximal rate of lactate flow from oligodendrocytes to neurons
        self.LacHalf = 1  # (g/min)  Concentration of oligodendrocyte lactate at which flow into neurons is half maximal

        self.KetMaxRate = 1  # (g/min)  Maximal rate of ketone flow from capillaries to neurons
        self.KetHalf = 1  # (g/ml)  Concentration of blood Ketone at which flow into neurons is half maximal   %Modif

        self.ATPdecay = 1  # (1/min) Rate of ATP self decay

        self.SynBase = 1  # (Hz ?)  Minimal synaptic activity
        self.SynMax = 10  # (Hz ?)  Maximal synaptic activity
        self.treshATP = 1  # (g/ml)  Concentration of ATP  at which Synaptic activated is influenced   %Modif
        self.tauATP = 1  # (g/ml)  Slope at which ATP concentration influences synaptic activity.
        self.treshCogn = 1  # (no units)  Cognition level at which synaptic activity is influenced
        self.tauCogn = 1  # (no units)  Rate at which cognitive activity influences synaptic activity

        # Parameters related to extracellular glutamate
        self.SynGlmate = 1  # (g/(min Hz)) Rate at which synaptic activity causes glutamate release
        self.GlmateAst = 1  # (1/min) Rate at which glutamate flows from the extracellular space into astrocytes
        self.GlmateOlig = 1  # (1/min) Rate at which glutamate flows from the extracellular space into oligodendrocytes.

        # Parameters related to quantities in astrocytes
        self.GlmineDecay = 1  # (1/min) decay rate of intracellular glutamine
        self.treshSynAct = 1  # (Hz)  Synaptic activity treshold at which astrocyte ATP is impacted
        self.tauSynAct = 1  # (Hz) Rate at which synaptic activity influence ATP in astrocyte
        self.treshGlmineAst = 1  # (g/ml) Concentration treshold of glutamine at which ATP in astrocyte will be inhibited
        self.tauGlmineAst = 0.5  # (g/ml) Rate at which glutamine inhibits ATP in astrocytes

        ## TODO: UTILE??
        self.GluHalfAst = 0.25  # (g/ml) Blood  glucose concentration at which glutamate flow in astrocyte is half maximal

        self.GlmateAstToLac = 1  #(1/min) Rate at which glutamate transforms to lactate in astrocytes
        self.GlmateAstToOlig = 0.5  # (1/min) Rate at which glutamate flows from astrocytes to oligodendrocytes
        self.LacAstToOlig = 1  #(1/min) Rate at which lactate flows from astrocytes to oligodendrocytes

# There is no need for extra parameters to describe quantities in oligodendrocites
