import yaml
from automata import Automata

class Lexer:
    def __init__(self, keywords):
        self.lexical_components = []
        self.file_path = "example.pas"
        self.final_states = {100,101,102,103,104,105,106,107,
                            108,109,110,111,112,113,114,115,
                            116,117,118,500,501,502,503,504}
        self.tokens = tuple()
        with open('transitions.yaml', 'r') as f:
            self.transitions = yaml.safe_load(f.read())

    dfa = Automata(transitions, final_states)

    def tokenize(self):
        lexeme = ""
        with open('example.pas', 'rb') as f:
            cur = ""
            while True:
                while not self.dfa.validated:
                    cur = f.read(1).decode('utf-8')
                    if cur == "":
                        self.dfa.change_state('EOF')
                        break
                    self.dfa.change_state(cur)
                    if cur.isalnum():
                        lexeme += cur

                self.lexical_components.append((lexeme, self.dfa.current_state))
                self.dfa.reset()
                lexeme = ""
                if cur == '':

                    break
                # else:
                #     print(lexeme)
                #     self.lexical_components.append(
                #        (lexeme, self.dfa.current_state))
                #     self.dfa.reset()
                #     lexeme = ""
                #     f.seek(-1,1)

                    #self.dfa.reset()
                    #self.change_state("EOF")
                
                # if not self.dfa.validated:
                #     self.dfa.change_state(c)
                #     if c == "":
                #         self.dfa.change_state("EOF")
                #         break
                # else:
                #     print(self.dfa.out_str,
                #           self.dfa.current_state,
                #           sep='->')
                #     self.dfa.reset()
