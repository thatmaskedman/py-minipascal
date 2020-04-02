#!/usr/bin/env python

import argparse
import yaml

def main():
    f = open("tokens.yaml", 'r')
    foo = yaml.safe_load(f.read())

    for v, k in foo.items():
        print(v,k)
    pass

if __name__ == "__main__":
    main()
