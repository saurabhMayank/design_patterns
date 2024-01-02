"""
Main class for demonstrating example of State Design Pattern
Github repo referenced
https://github.com/vicmar57/OOP-Design-Patterns/tree/master/StatePattern/src/StatePattern

"""
from state_design_pattern.gate import Gate

def run_simulation():
    metro_gate = Gate()
    metro_gate.pay()
    metro_gate.pay_failed()
    metro_gate.pay()
    metro_gate.pay_ok()
    metro_gate.enter()

if __name__ == "__main__":
    run_simulation()

"""
This code is giving circular import error if the classes are kept in different modules
 -> and this was expected because state change code


 If classes are kept in same module then that error does not come
"""