# Ne plus utiliser, avant rencontre avec Cunanne (2021-05-25)

class parameter():
    """
    Class defining the parameters of the model.
    """

    def __init__(self):
        # parameters from eating (constants for now...)
        self.eatGluSto = 1  # Glucose concentration in stomach
        self.eatKetSto = 1  # Ketone concentration in stomach
        self.eatInsu = 1  # Insulin
        self.eatCogn = 1  # Cognition

        # Parameters for digestion and metabolism in blood
        self.digestKet = 0.01  # (1/min) Speed at which ketones go from stomach to blood
        self.digestGlu = 0.01  # (1/min) Speed at which glucose go from stomach to blood
        self.decayGluBlood = 0.035  # (1/min) Speed at which glucose disappear from blood (not going to neural cells)
        self.decayKetBlood = 0.01  # (1/min) Speed at which ketones disappear from blood (not going to neural cells)

        # Parameters for GLUT transporters
        # self.GLUTNeuBase = 0.1  # (mole/min) Base activity of GLUT transporters activity in neurons
        # self.GLUTNeuMax = 0.5  # (mole/min) Maximal activity of GLUT transporters activity in neurons
        self.GLUTBase = 0.1  # (mole/min) Base activity of GLUT transporters activity
        self.GLUTMax = 0.5  # (mole/min) Maximal activity of GLUT transporters activity
        self.GLUTInsuHalf = 1  # (g/ml) Insulin concentration at which GLUT transporters are half activated
        # self.GLUTAstRate = 0.5  # (1/min) Activity of GLUT transporters in astrocytes
        # self.GLUTOligRate = 0.5  # (1/min) Activity of GLUT transporters in astrocytes

        # Parameters for quantities in neurons
        self.GluHalfNeu = 0.5  # (g/ml) Concentration of capillary glucose at which glucose transport by GLUT into
                            # neurons is half maximal

        self.VGluMaxNeu = 1  # (g/min)?? Maximal rate of glucose transformation to Acetyl-CoA in neuron.
        self.KGluHalfNeu = 0.5  # (g/ml)? Concentration of glucose in at which glucose transformation in Acetyl-CoA is half maximal in neuron.
        self.VLacMaxNeu = 1  # (g/min)?? Maximal rate of lactate transformation to Acetyl-CoA in neuron.
        self.KLacHalfNeu = 0.5  # (g/ml)? Concentration of lactate in at which lactate transformation in Acetyl-CoA is half maximal in neuron.
        self.VKetMaxNeu = 1  # (g/min)?? Maximal rate of ketone transformation to Acetyl-CoA in neuron.
        self.KKetHalfNeu = 0.5  # (g/ml)? Concentration of ketone in at which ketone transformation in Acetyl-CoA is half maximal in neuron.

        self.ACoAMaxRateNeu = 1  # (g /(ml min)?)  Maximal rate of Acetyl-CoA creation in neuron.
        self.ACoAHalfNeu = 1  # (g/ml ?) Acetyl-CoA concentration at which ATP creation is half maximal in neuron.

        self.LacOligToNeuMaxRate = 1  # (g/min) Maximal rate of lactate flow from oligodendrocytes to neurons
        self.LacHalf = 1  # (g/min)  Concentration of oligodendrocyte lactate at which flow into neurons is half maximal

        self.KetMaxRate = 1  # (g/min)  Maximal rate of ketone flow from capillaries to neurons
                             # 1.25 mu m gm^-1 min^-1 (source : Pollay, 1980)
        self.KetHalf = 1  # (g/ml)  Concentration of blood Ketone at which flow into neurons is half maximal
                              # 13.90 mM = 13.90 mmol/L = 13.90x10^−3 mol/L (source : Pollay, 1980)

        self.ATPdecay = 1  # (1/min) Rate of ATP self decay

        self.SynBase = 1  # (Hz ?)  Minimal synaptic activity
        self.SynMax = 10  # (Hz ?)  Maximal synaptic activity
        self.treshATP = 1  # (g/ml)  Concentration of ATP at which synaptic activity is influenced
        self.tauATP = 1  # (g/ml)  Slope at which ATP concentration influences synaptic activity.
        self.treshCogn = 1  # (no units)  Cognition level at which synaptic activity is influenced
        self.tauCogn = 1  # (no units)  Rate (slope) at which cognitive activity influences synaptic activity

        # Parameters related to extracellular glutamate
        self.SynGlmate = 1  # (g/(min Hz)) Rate at which synaptic activity causes glutamate release
        self.GlmateAst = 1  # (1/min) Rate at which glutamate flows from the extracellular space into astrocytes
        self.GlmateOlig = 1  # (1/min) Rate at which glutamate is used by oligodendrocytes.

        # Parameters related to quantities in astrocytes
        self.GlmateToGlmineAst = 6000  # (1/min) Rate at which glutamate is transformed to glutamine in astrocytes
        self.GlmineToATPAst = 500   # (1/min) Rate at which glutamine is transformed to ATP in astrocytes
        # self.ATPfromGlmine = 200  # (1/min) Rate at which ATP is formed form glutamine in astrocytes
        self.GlmineToNeu = 3000   # (1/min) Rate at which glutamine is transformed to ATP in astrocytes
        self.GlmineDecay = 1  # (1/min) decay rate of intracellular glutamine
        self.treshSynAct = 1  # (Hz)  Synaptic activity treshold at which astrocyte ATP is impacted
        # self.tauSynAct = 1  # (Hz) Rate at which synaptic activity influence ATP in astrocyte
        # self.treshGlmineAst = 1  # (g/ml) Concentration treshold of glutamine at which ATP in astrocyte will be inhibited
        # self.tauGlmineAst = 0.5  # (g/ml) Rate at which glutamine inhibits ATP in astrocytes

        self.GluHalfAst = 0.25  # (g/ml) Blood glucose concentration at which glucose flow in astrocyte is half maximal
        self.GluHalfOlig = 0.25  # (g/ml) Blood glucose concentration at which glucose flow in oligodendrocyte is half maximal

        # Valeurs pour Astrocyte (conversion en pyruvate)
        # Valeurs doivent être plus petites que pour neurones ...
        self.VGluMaxAst = 1  # (g/min)?? Maximal rate of glucose transformation to pyruvate in astrocyte.
        self.KGluHalfAst = 0.5  # (g/ml)? Concentration of glucose in at which glucose transformation in pyruvate is half maximal in astrocyte.
        self.VPyrMaxAst = 1  # (g/min)?? Maximal rate of pyruvate transformation to lactate in astrocyte.
        self.KPyrHalfAst = 0.5  # (g/ml)? Concentration of pyruvate in at which pyruvate transformation in lactate is half maximal in astrocyte.

        self.PyrMaxRateAst = 1  # (g /(ml min)?)  Maximal rate of Pyruvate creation in astrocyte.
        self.PyrHalfAst = 1  # (g/ml ?) Pyruvate concentration at which pyruvate creation is half maximal in astrocyte.

        # TODO: GluAstToLac devrait être variable selon l'entrée de glutamate (ANLS)... (à faire plus tard...)
        # self.GluAstToLac = 2  # (1/min) Rate at which glucose transforms to lactate in astrocytes
        self.GluAstToOlig = 0.5  # (1/min) Rate at which glucose flows from astrocytes to oligodendrocytes
        self.LacAstToOlig = 1  # (1/min) Rate at which lactate flows from astrocytes to oligodendrocytes
        # TODO: LacAstToNeu devrait être variable selon l'entrée de glutamate (ANLS)... (à faire plus tard...)
        self.LacAstToNeu = 1  # (1/min) Rate at which lactate flows from astrocytes to neuron

        self.PyrATPMaxRateAst = 1  # (g /(ml min)?)  Maximal rate of ATP creation from pyruvate in astrocyte
        self.PyrATPHalfAst = 1  # (g/ml ?) Pyruvate concentration at which ATP creation is half maximal in astrocyte

        self.treshATPAst = 1  # (g/ml)  Concentration of ATP at which ATP demand is half maximal (from pyruvate)
        self.tauATPAst = 0.2  # (g/ml)  Slope at which ATP concentration influences pyruvate conversion in ATP.

        # Oligo
        self.GlmateGLUT = 1.3  # (??) Glutamine impact on GLUT activity

        # Valeurs pour oligodendrocyte (conversion en pyruvate)
        # Valeurs doivent être plus petites que pour neurones ...
        self.VGluMaxOlig = 1  # (g/min)?? Maximal rate of glucose transformation to pyruvate in oligodendrocyte.
        self.KGluHalfOlig = 0.5  # (g/ml)? Concentration of glucose in at which glucose transformation in pyruvate is half maximal in oligodendrocyte.
        self.VPyrMaxOlig = 1  # (g/min)?? Maximal rate of pyruvate transformation to lactate in oligodendrocyte.
        self.KPyrHalfOlig = 0.5  # (g/ml)? Concentration of pyruvate in at which pyruvate transformation in lactate is half maximal in oligodendrocyte.

        self.PyrMaxRateOlig = 1  # (g /(ml min)?)  Maximal rate of Pyruvate creation in oligodendrocyte.
        self.PyrHalfOlig = 1  # (g/ml ?) Pyruvate concentration at which pyruvate creation is half maximal in oligodendrocyte.

        self.PyrATPMaxRateOlig = 1  # (g /(ml min)?)  Maximal rate of ATP creation from pyruvate in astrocyte
        self.PyrATPHalfOlig = 1  # (g/ml ?) Pyruvate concentration at which ATP creation is half maximal in astrocyte

        self.treshATPOlig = 1  # (g/ml)  Concentration of ATP at which ATP demand is half maximal (from pyruvate)
        self.tauATPOlig = 0.2  # (g/ml)  Slope at which ATP concentration influences pyruvate conversion in ATP.

