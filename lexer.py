import string
from automata import Automata
from error import Error

class Lexer:

    final_states = {100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
        111, 112, 113, 114, 115, 116, 117, 118, 500, 501, 502, 503, 504}

    write_states = {1,2,3,4,5,6,7,9,103,104,105,106,107,109,110,111,112,113,
                    115,118,119}

    def __init__(self, dfa, keywords, sourcefile):
        self.lexical_components = []
        self.file_path = sourcefile
        self.keywords = keywords
        self.dfa = dfa
        self.passes = False

    def append_token(self, token, token_id, li_num):
        self.lexical_components.append((token, token_id, li_num))

    def tokenize(self):
        self.dfa.set_write_states(self.write_states)
        f = open(self.file_path, 'r')
        for li_num, line in enumerate(f, 1):
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
                    if (self.dfa.next_state_final(char) and
                    self.dfa.current_state in {100, 101, 102}):
                            self.dfa.clear()
                            self.dfa.change_state(char)
                            self.dfa.make_string()
                            self.append_token(
                                self.dfa.out_string,
                                self.dfa.current_state,
                                li_num)
                            self.dfa.clear()
                            continue

                    self.dfa.clear()

            #End of line handling
            self.dfa.change_state('EOL')
            if self.dfa.validated:
                self.dfa.make_string()
                self.append_token(
                            lexeme,
                            self.dfa.current_state,
                            li_num)
                self.dfa.clear()

        f.close()

         # End of File error token handling
        self.dfa.change_state('EOF')
        self.dfa.make_string()
        if self.dfa.validated:
            self.append_token(
                self.dfa.out_string,
                self.dfa.current_state,
                li_num)

    def error_check(self):
        errors = {
            500: "Number was expected",
            501: "Unexpected end of file",
            502: "Unexpected end of line",
            503: "Ilegal character"
        }

        with open(self.file_path, 'r') as f:
            lines =  f.readlines()

        for tokens in self.lexical_components:
            token, value, li_num = tokens
            self.validated = True

            if value >= 500 <= 504:
                print(lines[li_num-1][:-1],
                    f"^Error at line {li_num}; {errors[value]}",
                      sep='\n')
                break

        self.passes = not value in Error.errors

    def print_tokens(self):
        for lexical in self.lexical_components:
            print(lexical)
