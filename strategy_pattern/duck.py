from strategy_pattern.IFly import IFly
from strategy_pattern.IQuack import IQuack

class Duck:
    """
    Duck class representing functionalities of Duck
    """
    def __init__(self, quack_behaviour: IQuack, fly_behaviour: IFly):
        self.quack_behaviour = quack_behaviour
        self.fly_behaviour = fly_behaviour
    
    def fly(self):
        """
        Fly method of the Duck
        Governed by Fly Behaviour passed at runtime
        """
        self.fly_behaviour.fly()
    
    def quack(self):
        """
        Quack method of the Duck
        Governed by Quack Behaviour passed at runtime
        """
        self.quack_behaviour.quack()
    
