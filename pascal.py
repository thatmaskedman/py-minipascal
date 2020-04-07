#!/usr/bin/env python

import argparse
import yaml
from automata import Automata
from lexer import Lexer

def main():
    argparser = argparse.ArgumentParser(description="A mini Pascal compiler")
    argparser.add_argument('source', help='Input source code')
    args = argparser.parse_args()

    source_file = open(args.source, 'rb')
    transitions = yaml.safe_load(open("transitions.yaml"))
    keywords = yaml.safe_load(open("keywords.yaml"))

    dfa = Automata(transitions,
                   {100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                    111, 112, 113, 114, 115, 116, 117, 118, 500, 501, 502,
                    503, 504})
    lexer = Lexer(dfa, keywords, source_file)
    lexer.tokenize()
    #lexer.print_tokens()
    lexer.error_check()
    #print(lexer.lexical_components)
    # dfa = Automata()
    # pascal = Lexer()
    #print(Lexical.transitions)

if __name__ == "__main__":
    main()
