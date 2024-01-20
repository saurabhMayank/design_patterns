from abc import ABC, abstractmethod


class IAnimalFactory(ABC):
    """
    Interface for Animal Factory classes
    """

    def __init__(self):
        pass
    
    @abstractmethod
    def create_animal(self):
        """
        This function will handle the logic of
        i) Preprocessing logic before instantiation of animal class
        ii) Instantiating animal object by one of its subclasses that implements the interface
        iii) Post processing logic after instantiation of animal class
        """
        pass