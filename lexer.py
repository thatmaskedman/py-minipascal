import string
from automata import Automata

class Lexer:

    final_states = {100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
        111, 112, 113, 114, 115, 116, 117, 118, 500, 501, 502, 503, 504}

    write_states = {1,2,3,4,5,6,7,9,103,104,105,106,110, 112, 113, 115, 118}

    def __init__(self, dfa, keywords, sourcefile):
        self.lexical_components = []
        self.file_path = "example.pas"
        self.sourcefile = sourcefile
        self.keywords = keywords
        self.dfa = dfa

    def append_token(self, token, token_id, li_num):
        self.lexical_components.append((token, token_id, li_num))

    def tokenize(self):
        self.dfa.set_write_states(self.write_states)
        with open(self.file_path) as f:
            lines = f.readlines()

        for li_num, line in enumerate(lines):
            for char in line:
                self.dfa.change_state(char)
                if self.dfa.validated:
                    self.dfa.make_string()
                    lexeme = self.dfa.out_string
                    if lexeme in self.keywords:
                        self.append_token(
                            lexeme,
                             self.keywords[lexeme],
                             li_num)
                    else:
                        self.append_token(
                            lexeme,
                            self.dfa.current_state,
                            li_num)
                    # print(lexeme,'->', self.dfa.current_state)
                    if self.dfa.next_state_final(char) and self.dfa.current_state == 100:
                        self.dfa.clear()
                        self.dfa.change_state(char)
                        self.dfa.make_string()
                        self.append_token(
                            self.dfa.out_string,
                            self.dfa.current_state,
                            li_num)
                        # print(self.dfa.out_string,'->', self.dfa.current_state)
                        self.dfa.clear()
                        continue
                    self.dfa.clear()

    def print_tokens(self):
        for lexical in self.lexical_components:
            print(lexical)
