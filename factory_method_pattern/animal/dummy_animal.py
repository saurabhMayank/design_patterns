from factory_method_pattern.IAnimal import IAnimal

class DummyAnimal(IAnimal):
    """
    Dummy Animal class implementing the IAnimal Interface
    """

    def __init__(self):
        pass
    
    def say_hello(self):
        pass