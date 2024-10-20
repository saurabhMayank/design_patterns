# before refactoring
class Order:
    def __init__(self):
        self.state = "created"

    def next_state(self):
        if self.state == "created":
            self.state = "shipped"
        elif self.state == "shipped":
            self.state = "delivered"
        elif self.state == "delivered":
            print("Order already delivered")
    
    def previous_state(self):
        if self.state == "delivered":
            self.state = "shipped"
        elif self.state == "shipped":
            self.state = "created"
        elif self.state == "created":
            print("Order is in initial state")

    def print_status(self):
        print(f"Order is currently {self.state}")
        

# Example usage
order = Order()
order.print_status()   # Order is currently created
order.next_state()     # Transition to shipped
order.print_status()   # Order is currently shipped
order.next_state()     # Transition to delivered
order.print_status()   # Order is currently delivered
order.previous_state() # Transition back to shipped
order.print_status()   # Order is currently shipped




# after refactoring
class OrderState:
    def next(self, order):
        raise NotImplementedError

    def previous(self, order):
        raise NotImplementedError

    def print_status(self):
        raise NotImplementedError


class CreatedState(OrderState):
    def next(self, order):
        order.state = ShippedState()

    def previous(self, order):
        print("Order is in the initial state.")

    def print_status(self):
        print("Order is in created state.")


class ShippedState(OrderState):
    def next(self, order):
        order.state = DeliveredState()

    def previous(self, order):
        order.state = CreatedState()

    def print_status(self):
        print("Order is in shipped state.")


class DeliveredState(OrderState):
    def next(self, order):
        print("Order already delivered.")

    def previous(self, order):
        order.state = ShippedState()

    def print_status(self):
        print("Order is in delivered state.")


class Order:
    def __init__(self):
        self.state = CreatedState()  # Start in the created state

    def next_state(self):
        self.state.next(self)

    def previous_state(self):
        self.state.previous(self)

    def print_status(self):
        self.state.print_status()


# Example usage
order = Order()
order.print_status()   # Order is in created state
order.next_state()     # Transition to shipped state
order.print_status()   # Order is in shipped state
order.next_state()     # Transition to delivered state
order.print_status()   # Order is in delivered state
order.previous_state() # Transition back to shipped state
order.print_status()   # Order is in shipped state
