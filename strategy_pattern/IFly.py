from abc import ABC, abstractmethod

class IFly(ABC):
    """
    Interface for flying behaviour
    """
    def __init__(self):
        pass
    
    @abstractmethod
    def fly(self):
        pass

    