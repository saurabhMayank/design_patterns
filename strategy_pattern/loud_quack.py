from strategy_pattern.IQuack import IQuack

class LoudQuack(IQuack):
    """
    Class for Loud quacking
    """

    def quack(self):
        print("Loud Quacking Behaviour")