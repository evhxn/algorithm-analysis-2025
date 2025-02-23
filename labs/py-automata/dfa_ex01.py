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
    A1 = dfa.DFA(
        Q={1, 2, 3, 4},
        Sigma={'a', 'b'},
        delta={
            (1, 'a'): 2, (1, 'b'): 4,
            (2, 'a'): 2, (2, 'b'): 3,
            (3, 'a'): 4, (3, 'b'): 4,
            (4, 'a'): 4, (4, 'b'): 4
        },
        q0=1,
        F={3}
    )
    
    # todo: instantiate accordingly
    A2 = dfa.DFA(
        Q={1, 2, 3},
        Sigma={'a', 'b'},
        delta={
            (1, 'a'): 2, (1, 'b'): 1,
            (2, 'a'): 3, (2, 'b'): 1,
            (3, 'a'): 3, (3, 'b'): 2
        },
        q0=1,
        F={3}
    )
    
    words = generate_words()
    automata = [A1, A2]
    
    # test words on automata
    for X in automata:
         print(f"{X.__repr__()}")
         for w in words:
            print(f"{w}: {X.run(w)}")
         print("\n")

__main__()