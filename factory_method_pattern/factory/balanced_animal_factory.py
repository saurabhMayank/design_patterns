from factory_method_pattern.animal.cat import Cat
from factory_method_pattern.animal.dog import Dog
from factory_method_pattern.animal.duck import Duck
from factory_method_pattern.animal.dummy_animal import DummyAnimal
from factory_method_pattern.IAnimalFactory import IAnimalFactory

import random

class BalancedAnimalFactory(IAnimalFactory):
    def __init__(self, max_count_per_type):
        self.max_count_per_type = max_count_per_type
        # counter of classes
        # all the keys in the dict are class representations
        # they are not strings
        self.current_count = {Cat: 0, Duck: 0, Dog: 0}

    def create_animal(self):
        available_types = [animal_type for animal_type, count in self.current_count.items() if count < self.max_count_per_type]

        if not available_types:
            return None  # Limit reached for all types

        # print("---available types---")
        # print(available_types)
        animal_type = random.choice(available_types)
        # print("---animal type-----")
        # print(animal_type)
        self.current_count[animal_type] += 1

        if animal_type == Cat:
            return Cat()
        elif animal_type == Duck:
            return Duck()
        else:
            return Dog()




# class BalancedAnimalFactory(IAnimalFactory):
#     """
#     Count of all the animals generated should be same
#     Maintain a counter for all the animals
#     If the counter is 0 -> then only generate the animal
#     When counter of all elements is > 0 -> then all the animals
#     are generated once -> reset the counter
#     """
#     dog_counter = 0
#     cat_counter = 0
#     duck_counter = 0

#     def __init__(self):
#         self.reset_counter_once_animals_generated()
    
#     def reset_counter_once_animals_generated(self):
#         # global dog_counter
#         # global cat_counter
#         # global duck_counter
#         # if counter of all the animals generated > 0
#         # i.e. all elements are generated once
#         if BalancedAnimalFactory.dog_counter > 0 and BalancedAnimalFactory.cat_counter > 0 and BalancedAnimalFactory.duck_counter > 0:
#             dog_counter = 0
#             cat_counter = 0
#             duck_counter = 0

#     def create_animal(self):
#         """
#         Create animals in a balanced count
#         """
#         random_number = random.randint(1, 3)

#         print("---random number---")
#         print(random_number)
#         print("\n")

#         if random_number == 1 and BalancedAnimalFactory.cat_counter == 0:
#             cat_obj = Cat()
#             BalancedAnimalFactory.cat_counter = BalancedAnimalFactory.cat_counter + 1
#             # print("---returning cat---")
#             # print(cat_obj)
#             # print("\n")
#             return cat_obj
#         else:
#             return DummyAnimal()


#         if random_number == 2 and BalancedAnimalFactory.dog_counter == 0:
#             dog_obj = Dog()
#             BalancedAnimalFactory.dog_counter = BalancedAnimalFactory.dog_counter + 1
#             # print("---returning dog---")
#             # print(dog_obj)
#             # print("\n")
#             return dog_obj
#         else:
#             return DummyAnimal()
        

#         if random_number == 3 and BalancedAnimalFactory.duck_counter == 0:
#             duck_obj = Duck()
#             BalancedAnimalFactory.duck_counter = BalancedAnimalFactory.duck_counter + 1
#             # print("---returning duck---")
#             # print(duck_obj)
#             # print("\n")
#             return duck_obj
#         else:
#             return DummyAnimal()
        
            

