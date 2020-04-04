#!/usr/bin/env python

import argparse
import yaml
from automata import Automata
from lexical import Lexical

def main():
    Lexical.analyze()
    #print(Lexical.transitions)

if __name__ == "__main__":
    main()
