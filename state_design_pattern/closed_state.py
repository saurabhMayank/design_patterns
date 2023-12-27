"""
Closed Gate State
In thi state -> Gate is closed
"""
from state_design_pattern.IGateState import IGateState

class ClosedGateState(IGateState):
    def __init__(self, gate):
        self.gate = gate

    def pay(self):
        pass

    def pay_ok(self):
        pass

    def pay_failed(self):
        pass

    def enter(self):
        pass
