from factory_method_pattern.animal.cat import Cat
from factory_method_pattern.animal.dog import Dog
from factory_method_pattern.animal.duck import Duck
from factory_method_pattern.IAnimalFactory import IAnimalFactory

class BalancedAnimalFactory(IAnimalFactory):
    """
    Count of all the animals generated should be same
    Maintain a counter for all the animals
    If the counter is 0 -> then only generate the animal
    When counter of all elements is > 0 -> then all the animals
    are generated once -> reset the counter
    """
    dog_counter = 0
    cat_counter = 0
    duck_counter = 0

    def __init__(self):
        self.reset_counter_once_animals_generated()
    
    def reset_counter_once_animals_generated(self):
        global dog_counter
        global cat_counter
        global duck_counter

        # if counter of all the animals generated > 0
        # i.e. all elements are generated once
        if global dog_counter and global cat_counter and global duck_counter:
            dog_counter = 0
            cat_counter = 0
            duck_counter = 0

    def create_animal(self):
        """
        Create animals in a balanced count
        """
        random_number = random.randint(1, 3)

        if random_number == 1 and cat_counter == 0:
            cat_obj = Cat()
            cat_counter = cat_counter + 1
            return cat_obj
        elif random_number == 2 and dog_counter == 0:
            dog_obj = Dog()
            dog_counter = dog_counter + 1
            return dog_obj
        elif random_number == 3 and duck_counter == 0:
            duck_obj = Duck()
            duck_counter = duck_counter + 1
            return duck_obj
            

