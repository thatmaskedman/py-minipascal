#!/usr/bin/env python

import argparse
import yaml
from automata import Automata
from lexer import Lexer

def main():
    argparser = argparse.ArgumentParser(description="A mini Pascal compiler")
    argparser.add_argument('source', help='Input source code')
    args = argparser.parse_args()
    print(args.source)
    # dfa = Automata()
    # pascal = Lexer()
    #print(Lexical.transitions)

if __name__ == "__main__":
    main()
