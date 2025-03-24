import dfa

def __main__():
    # instantiate DFA A using same automaton in dfa_ex03.py
    A = dfa.DFA(
        Q={1, 2, 3, 4},
        Sigma={'a', 'b'},
        delta={
            (1, 'a'): 2, (1, 'b'): 4,
            (2, 'a'): 3, (2, 'b'): 4,
            (3, 'a'): 3, (3, 'b'): 3,
            (4, 'a'): 2, (4, 'b'): 3
        },
        q0=1,
        F={2, 4}
    )
    # instantiate DFA B
    B = dfa.DFA(
        Q={0, 1},
        Sigma={'a', 'b'},
        delta={
            (0, 'a'): 1, (0, 'b'): 0,
            (1, 'a'): 0, (1, 'b'): 1
        },
        q0=0,
        F={0}
    )
    # c is intersection
    C = A.both(B)

    test_words = ["", "a", "b", "ab", "ba", "aa", "bb", "aba", "aab", "abb", "bba", "bab"]

    print("Testing DFA A:")
    for word in test_words:
        print(f"{word}: {A.run(word)}")

    print("\nTesting DFA B:")
    for word in test_words:
        print(f"{word}: {B.run(word)}")

    print("\nTesting DFA C (Intersection of A and B):")
    for word in test_words:
        print(f"{word}: {C.run(word)}")

__main__()
