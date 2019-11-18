# Original implementation
class State:
    def __init__(self):
        self.state = 'A'

    def action(self, x):
        if self.state == 'A':
            # Action for A
            self.state = 'B'

        elif self.state == 'B':
            # Action for B
            self.state = 'C'

        elif self.state == 'C':
            # Action for C
            self.state = 'A'

# Alternative implementation
class State:
    def __init__(self):
        self.new_state(State_A)
    def new_state(self, state):
        self.__class__ = state
    def action(self, x):
        raise NotImplementedError()

class State_A(State):
    def action(self, x):
        # Action for A
        self.new_state(State_B)

class State_B(State):
    def action(self, x):
        # Action for B
        self.new_state(State_C)

class State_C(State):
    def action(self, x):
        # Action for C
        self.new_state(State_A)