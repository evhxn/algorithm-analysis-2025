import dfa

# generate words for testing
def generate_words():
    words = []
    alphabet = ['a', 'b']
    for first in alphabet:
        for second in alphabet:
            for third in alphabet:
                words.append(first + second + third)
    return words

def __main__() :
    
    # todo: instantiate accordingly
    A1 = dfa.DFA(...)
    
    # todo: instantiate accordingly
    A2 = dfa.DFA(...)
    
    words = generate_words()
    automata = [A1, A2]
    
    # test words on automata
    for X in automata:
         print(f"{X.__repr__()}")
         for w in words:
            print(f"{w}: {X.run(w)}")
         print("\n")

__main__()