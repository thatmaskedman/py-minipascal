#!/usr/bin/env python

import argparse
import yaml
from automata import Automata
from lexer import Lexer

final_states = {100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                111, 112, 113, 114, 115, 116, 117, 118, 119, 500, 501, 502,
                503, 504}

write_states = {1,2,3,4,5,6,7,9,103,104,105,106,107,109,110,111,112,113,
                115,116,118}

def main():
    argparser = argparse.ArgumentParser(
        description="A mini Pascal compiler implemented in Python")
    argparser.add_argument('source', help='Input source code')
    args = argparser.parse_args()

    transitions = yaml.safe_load(open("transitions.yaml"))
    keywords = yaml.safe_load(open("keywords.yaml"))

    dfa = Automata(transitions, final_states, write_states)

    lexer = Lexer(dfa, keywords, args.source)
    lexer.tokenize()
    lexer.error_check()
    if lexer.passes:
        print("Lexical analysis complete, no errors found.")
        lexer.print_tokens()


if __name__ == "__main__":
    main()
