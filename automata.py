class Automata:
    def __init__(self, transitions: dict, final_states: set):
        self.final_states = final_states
        self.transitions = transitions
        self.current_state = 0
        self.out_str = ""
        self.validated = False
        self.rejected = False

    def __str__(self):
        pass

    def reset(self):
        self.out_str = ""
        self.current_state = 0
        self.validated = False
        self.rejected = False

    def change_state(self, c : chr):
        # if not self.validated and not self.rejected:
            # if c not in self.transitions:
                # self.rejected = True
            # else:
        key = ""
        if self.current_state in self.final_states:
            self.validated = True
        else:
            for k in self.transitions[self.current_state].keys():
                if c in k:
                    key = k
                    break
            if k == "":
                key = "\xfe"
            self.current_state = self.transitions[self.current_state][key]
            self.out_str += c
