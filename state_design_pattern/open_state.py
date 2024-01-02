# """
# Closed Gate State
# In thi state -> Gate is closed
# """
# from state_design_pattern.IGateState import IGateState
# from state_design_pattern.processing_pay_state import ProcessingPayState
# from state_design_pattern.closed_state import ClosedGateState
# import time

# class OpenGateState(IGateState):
#     def __init__(self, gate):
#         self.gate = gate

#     def pay(self):
#         print("Payment is already done, gate is already open")

#     def pay_ok(self):
#         print("payment successful -> Gate is open")
        
#         # after 1000 ms closed the gate
#         time.sleep(1000)
#         self.gate.change_state(ClosedGateState(self.gate))

#     def pay_failed(self):
#         # keep gate closed
#         # gate will be in processing 
#         # do nothing from here
#         print("Gate is already open, no need to initiate pay")
#         # self.gate.change_state(ClosedGateState(self.gate))

#     def enter(self):
#         print("Gate is already open pls enter")
