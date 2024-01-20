from abc import ABC, abstractmethod


class IAnimal(ABC):
    """
    Interface for Animal classes
    """

    def __init__(self):
        pass
    
    @abstractmethod
    def say_hello(self):
        pass

