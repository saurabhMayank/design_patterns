# """
# Closed Gate State
# In thi state -> Gate is closed
# """
# from state_design_pattern.IGateState import IGateState
# from state_design_pattern.processing_pay_state import ProcessingPayState

# class ClosedGateState(IGateState):
#     def __init__(self, gate):
#         self.gate = gate

#     def pay(self):
#         print("Gate Closed. Payment in processing")
#         self.gate.change_state(ProcessingPayState(self.gate))

#     def pay_ok(self):
#         print("do nothing")

#     def pay_failed(self):
#         # keep gate closed
#         # gate will be in processing 
#         # do nothing from here
#         print("gate is already closed")

#     def enter(self):
#         print("Gate Closed : Cannot enter without paying")
