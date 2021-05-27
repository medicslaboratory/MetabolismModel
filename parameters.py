
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