# Product class representing the final pizza
class Pizza:
    def __init__(self):
        self.toppings = []
        self.crust = None
        self.size = None
    
    def add_topping(self, topping):
        self.toppings.append(topping)
    
    def set_crust(self, crust):
        self.crust = crust
    
    def set_size(self, size):
        self.size = size
    
    def __str__(self):
        return f"Pizza with {', '.join(self.toppings)} toppings, {self.crust} crust, and size {self.size}"

# Abstract builder class
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()
    
    def add_toppings(self):
        pass
    
    def set_crust(self):
        pass
    
    def set_size(self):
        pass
    
    def get_pizza(self):
        return self.pizza

# Concrete builder class for Margherita pizza
class MargheritaPizzaBuilder(PizzaBuilder):
    def add_toppings(self):
        self.pizza.add_topping("cheese")
        self.pizza.add_topping("tomatoes")
        self.pizza.add_topping("fresh basil")
    
    def set_crust(self):
        self.pizza.set_crust("thin")
    
    def set_size(self):
        self.pizza.set_size("medium")

# Concrete builder class for Pepperoni pizza
class PepperoniPizzaBuilder(PizzaBuilder):
    def add_toppings(self):
        self.pizza.add_topping("cheese")
        self.pizza.add_topping("pepperoni")
    
    def set_crust(self):
        self.pizza.set_crust("thick")
    
    def set_size(self):
        self.pizza.set_size("large")

# Director class that oversees the building process
class Director:
    def __init__(self, builder):
        self.builder = builder
    
    def construct_pizza(self):
        self.builder.add_toppings()
        self.builder.set_crust()
        self.builder.set_size()

# Client code
if __name__ == '__main__':
    margherita_builder = MargheritaPizzaBuilder()
    director = Director(margherita_builder)
    director.construct_pizza()
    margherita_pizza = margherita_builder.get_pizza()
    print(margherita_pizza)
    
    pepperoni_builder = PepperoniPizzaBuilder()
    director = Director(pepperoni_builder)
    director.construct_pizza()
    pepperoni_pizza = pepperoni_builder.get_pizza()
    print(pepperoni_pizza)
