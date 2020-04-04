from automata import Automata

class Lexer:
    def __init__(self, dfa, keywords, source):
        self.lexical_components = []
        #self.file_path = "example.pas"
        # self.final_states = {100,101,102,103,104,105,106,107,
        #                     108,109,110,111,112,113,114,115,
        #                     116,117,118,500,501,502,503,504}
        # with open('transitions.yaml', 'r') as f:
        #     self.transitions = yaml.safe_load(f.read())
        self.dfa = dfa
        self.sourcepath = sourcepath

    def tokenize(self):
        lexeme = ""
