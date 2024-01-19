from factory_method_pattern.factory.random_animal_factory import RandomAnimalFactory
from factory_method_pattern.factory.balanced_animal_factory import BalancedAnimalFactory

# create animals in the zoo using random animal factory
random_animal_factory_obj = RandomAnimalFactory()
balanced_animal_factory_obj = BalancedAnimalFactory()

print(" Animals generated randomly ")
print("\n")

for i in range(0, 17):
    animal_obj = random_animal_factory_obj.create_animal()
    animal_obj.say_hello()

print("----------------------------------")

print(" Animals generated in a balanced way ")
print("\n")

for i in range(0, 17):
    animal_obj = balanced_animal_factory_obj.create_animal()
    animal_obj.say_hello()