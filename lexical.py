import yaml
from automata import Automata

class Lexical:
    lexical_components = []
    file_path = "example.pas"
    final_states = {100,101,102,103,104,105,106,107,
                    108,109,110,111,112,113,114,115,
                    116,117,118,500,501,502,503,504}

    with open('transitions.yaml', 'r') as f:
        transitions = yaml.safe_load(f.read())
        f.close()

    dfa = Automata(transitions, final_states)

    def analyze():
        with open('example.pas') as f:
            print(f.readline())
            print(f.seek(-1,1))
