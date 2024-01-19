from strategy_pattern.IQuack import IQuack

class LoudQuack(IQuack):
    """
    Class for Loud quacking
    """

    def __init__(self):
        pass

    def quack(self):
        print("Loud Quacking Behaviour")