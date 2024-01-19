from factory_method_pattern.IAnimal import IAnimal

class Dog(IAnimal):
    """
    Dog class implementing the IAnimal Interface
    """

    def __init__(self):
        pass
    
    def say_hello(self):
        print("Hello I am a dog!")