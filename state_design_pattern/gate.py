"""
This is the Gate Class
Through Object of this User will interact

Initial state of Gate will be closed
"""
from state_design_pattern.IGateState import IGateState

class Gate:
    def __init__(self):
        # initially gate is closed
        self.gate_state = ClosedGateState(self)

    
    def pay(self):
        return self.gate_state.pay()

    
    def pay_ok(self):
        return self.gate_state.pay_ok()

    def pay_failed(self):
        return self.gate_state.pay_failed()
    
    def enter(self):
        return self.gate_state.enter()

    def change_state(self, new_gate_state: IGateState):
        """
        change the gate state to the new_gate_state
        that is passed as an argument to the change state function
        when there is a transition needed from one state to another
        then change_state function is called
        """
        self.gate_state = new_gate_state


class ClosedGateState(IGateState):
    def __init__(self, gate):
        self.gate = gate

    def pay(self):
        print("Gate Closed. Payment in processing")
        self.gate.change_state(ProcessingPayState(self.gate))

    def pay_ok(self):
        print("do nothing")

    def pay_failed(self):
        # keep gate closed
        # gate will be in processing 
        # do nothing from here
        print("gate is already closed")

    def enter(self):
        print("Gate Closed : Cannot enter without paying")


class OpenGateState(IGateState):
    def __init__(self, gate):
        self.gate = gate

    def pay(self):
        print("Payment is already done, gate is already open")

    def pay_ok(self):
        print("payment successful -> Gate is open")
        
        # after 1000 ms closed the gate
        time.sleep(1000)
        self.gate.change_state(ClosedGateState(self.gate))

    def pay_failed(self):
        # keep gate closed
        # gate will be in processing 
        # do nothing from here
        print("Gate is already open, no need to initiate pay")
        # self.gate.change_state(ClosedGateState(self.gate))

    def enter(self):
        print("Gate is already open pls enter")


class ProcessingPayState(IGateState):

    def __init__(self, gate):
        self.gate = gate

    def pay(self):
        print("Payment is in processing, no need to pay again")

    def pay_ok(self):
        print("payment is successful gate is opening")
        # change state to open
        self.gate.change_state(OpenGateState(self.gate))

    def pay_failed(self):
        print("payment is failed, gate will be closed, Pay again")
        # change state to open
        self.gate.change_state(ClosedGateState(self.gate))

    def enter(self):
        print("Wait payment is in process")