class IAnimalFactory():
    """
    Interface for Animal Factory classes
    """

    def __init__(self):
        pass
    
    def create_animal(self):
        """
        This function will handle the logic of
        i) Preprocessing logic before instantiation of animal class
        ii) Instantiating animal object by one of its subclasses that implements the interface
        iii) Post processing logic after instantiation of animal class
        """
        pass