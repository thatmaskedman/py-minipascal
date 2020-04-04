class Automata:
    def __init__(self, transitions, final_states):
        self.final_states = final_states
        self.transitions = transitions
        self.current_state = 0
        self.next_state = 0
        self.validated = False

    def __str__(self):
        pass

    def reset(self):
        self.current_state = 0
        self.validated = False

    def change_state(self, d):
        self.next_state = self.transitions[self.current_state][d]
        if self.next_state in self.final_states:
            self.current_state = self.transitions[self.current_state][d]
            self.validated = True
        else:
            print("VALID:", d, end=", ")
            self.current_state = self.transitions[self.current_state][d]
