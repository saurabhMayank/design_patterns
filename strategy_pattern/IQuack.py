from abc import ABC, abstractmethod


class IQuack(ABC):
    """
    Interface for quacking behaviour
    """

    def __init__(self):
        pass
    
    @abstractmethod
    def quack(self):
        pass