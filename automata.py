class Automata:
    def __init__(self, transitions, final_states):
        self.final_states = final_states
        self.transitions = transitions
        self.current_state = 0
        self.validated = False

    def __str__(self):
        pass

    def reset(self):
        self.current_state = 0
        self.validated = False

    def change_state(self, d):
        if self.current_state in self.final_states:
            self.validated = True
        else:
            self.validated = False
            self.current_state = self.transitions[self.current_state][d]
