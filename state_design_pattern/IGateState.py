"""
Gate State Interface
Will have methods -> These methods will be implemented by concrete classes that implements GateStateInterface

pay()
payOk()
payFailed()
enter()
"""

class IGateState:
    def __init__():
        pass

    def pay():
        """
        User is trying to pay at the gate
        """
        pass

    def pay_ok():
        """
        Payment done by user is successful
        """
        pass

    def pay_failed():
        """
        Payment done by user has failed
        """
        pass

    def enter():
        """
        After payment is successful -> user is allowed to enter
        from the gate
        """
        pass