#!/usr/bin/env python

import argparse
import yaml
from automata import Automata
from lexer import Lexer

final_states = {100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                111, 112, 113, 114, 115, 116, 117, 118, 500, 501, 502,
                503, 504}

def main():
    argparser = argparse.ArgumentParser(description="A mini Pascal compiler")
    argparser.add_argument('source', help='Input source code')
    args = argparser.parse_args()

    transitions = yaml.safe_load(open("transitions.yaml"))
    keywords = yaml.safe_load(open("keywords.yaml"))

    dfa = Automata(transitions, final_states)

    lexer = Lexer(dfa, keywords, args.source)
    lexer.tokenize()
    lexer.error_check()
    if lexer.validated:
        print("Lexical analysis complete, no errors found.")


if __name__ == "__main__":
    main()
