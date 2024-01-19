from strategy_pattern.IQuack import IQuack

class SimpleQuack(IQuack):
    """
    Class for Simple quacking
    """

    def quack(self):
        print("Simple Quacking Behaviour")