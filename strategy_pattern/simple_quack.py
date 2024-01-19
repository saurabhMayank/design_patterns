from strategy_pattern.IQuack import IQuack

class SimpleQuack(IQuack):
    """
    Class for Simple quacking
    """

    def __init__(self):
        pass

    def quack(self):
        print("Simple Quacking Behaviour")