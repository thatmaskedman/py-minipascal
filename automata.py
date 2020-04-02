class Automata:

    """Docstring for Automata. """

    def __init__(self):
        """TODO: to be defined. """
        self.states = {} 
        self.input_str = ""
        self.output = ""
        self.validated = false
        pass

    def __str__(self):
        pass

    def add_state(self, name, transitions, destination):
        self.states.update(name: transitions)
    
    def test(self, test):
        current_state = 0
        for c in input_string:
            current_state = self.states[current_state][c]
            print(current_state)

    def input_string(self, input_str):
        self.input_str = input_str
    
    def validate():
        pass
