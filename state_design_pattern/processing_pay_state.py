from state_design_pattern.IGateState import IGateState
from state_design_pattern.open_state import OpenGateState

class ProcessingPayState(IGateState):

    def __init__(self, gate):
        self.gate = gate

    def pay(self):
        print("Payment is in processing, no need to pay again")

    def pay_ok(self):
        print("payment is successful gate is opening")
        # change state to open
        self.gate.change_state(new OpenGateState(self.gate))

    def pay_failed(self):
        print("payment is failed, gate will be closed, Pay again")
        # change state to open
        self.gate.change_state(new ClosedGateState(self.gate))

    def enter(self):
        print("Wait payment is in process")