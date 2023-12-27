"""
This is the Gate Class
Through Object of this User will interact

Initial state of Gate will be closed
"""
from state_design_pattern.IGateState import IGateState
from state_design_pattern.closed_state import ClosedGateState


class Gate:
    def __init__(self):
        self.gate_state = ClosedGateState()

    
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
        """
        self.gate_state = new_gate_state



