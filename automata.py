import string

class Automata:
    def __init__(self, transitions, final_states, write_states):
        self.transitions = transitions
        self.final_states = final_states
        self.input_chars = []
        self.write_states = write_states
        self.trans_states = []
        self.current_state = 0
        self.out_string = ""
        self.validated = False

    def change_state(self, d):
        try:
            self.current_state = self.transitions[self.current_state][self.char_type(d)]
            self.trans_states.append(self.current_state)
            self.input_chars.append(d)
            if self.current_state in self.final_states:
                self.validated = True

        except KeyError:
            self.validated = False

    def clear(self):
        self.input_chars = []
        self.trans_states = []
        self.current_state = 0
        self.out_string = ""
        self.validated = False

    def make_string(self):
        if len(self.trans_states) > 1:
            out_string = []
            for d, s in zip(self.input_chars, self.trans_states):
                if s in self.write_states:
                    out_string.append(d)
            self.out_string = "".join(out_string)
        else:
            self.out_string = "".join(self.input_chars)

    def char_type(self, c):
        if c in "_" + string.ascii_letters:
            return "ALPHA"
        elif c in string.digits:
            return "NUM"
        elif c == "EOF":
            return "EOF"
        elif c == "EOL":
            return "EOL"
        elif c in "=+-*<>:.,;(){}\" \n\t":
            return c
        else:
            return "OC"

    
