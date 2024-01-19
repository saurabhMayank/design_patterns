from factory_method_pattern.animal.cat import Cat
from factory_method_pattern.animal.dog import Dog
from factory_method_pattern.animal.duck import Duck
from factory_method_pattern.IAnimalFactory import IAnimalFactory

import random

class RandomAnimalFactory(IAnimalFactory):
    """
    Factory class for generating animals randomly
    """

    def __init__(self):
        pass
    
    def create_animal(self):
        """
        Get a random number between (1, 3)
        Based on the number create a animal and return its object
        """
        random_number = random.randint(1, 3)

        if random_number == 1:
            cat_obj = Cat()
            return cat_obj
        elif random_number == 2:
            dog_obj = Dog()
            return dog_obj
        else:
            duck_obj = Duck()
            return duck_obj