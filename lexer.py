import string
from automata import Automata

class Lexer:

    final_states = {100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
        111, 112, 113, 114, 115, 116, 117, 118, 500, 501, 502, 503, 504}

    write_states = {1,2,3,4,5,6,7,9,103,104,105,106,107,109,110,111,112,113,
                    115,118}

    errors = {
            500: "Number was expected",
            501: "Unexpected end of file",
            502: "Unexpected end of line",
            503: "Ilegal character"
        }

    def __init__(self, dfa, keywords, sourcefile):
        self.lexical_components = []
        self.file_path = sourcefile
        self.keywords = keywords
        self.dfa = dfa
        self.passes = False

    def create_token(self, string, value, li_num):
        print(string)
        if string in self.keywords:
            self.lexical_components.append((string,
                                            self.keywords[string],
                                            li_num))
        else:
            self.lexical_components.append((string, value, li_num))

    def tokenize(self):
        self.dfa.set_write_states(self.write_states)
        f = open(self.file_path, 'r')

        look_ahead = False
        for li_num, line in enumerate(f, 1):
            for char in line:
                self.dfa.change_state(char)
                if self.dfa.validated:
                    self.dfa.make_string()
                    self.create_token(self.dfa.out_string,
                                      self.dfa.current_state,
                                      li_num)

                    if (self.dfa.next_state_final(char)
                        and self.dfa.current_state in {100,101,102}):
                        self.dfa.clear()
                        self.dfa.change_state(char)
                        self.dfa.make_string()
                        self.create_token(self.dfa.out_string,
                                          self.dfa.current_state,
                                          li_num,)
                    self.dfa.clear()

            self.dfa.change_state('EOL')
            if self.dfa.validated:
                self.create_token(self.dfa.out_str,
                                self.dfa.current_state,
                                li_num)
                self.dfa.clear()

        f.close()

         # End of File error token handling
        self.dfa.change_state('EOF')
        self.dfa.make_string()

    def error_check(self):
        with open(self.file_path, 'r') as f:
            lines =  f.readlines()

        # for tokens in self.lexical_components:
        #     token, value, li_num = tokens
        #     self.validated = True

        #     if value >= 500 <= 504:
        #         print(lines[li_num-1][:-1],
        #             f"^Error at line {li_num}; {self.errors[value]}",
        #               sep='\n')
        #         break

        # self.passes = not value in self.errors
        self.passes = True

    def print_tokens(self):
        for lexical in self.lexical_components:
            print(lexical)
