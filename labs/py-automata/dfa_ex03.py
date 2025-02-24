import dfa

def __main__() :
    
    # todo: instantiate accordingly
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
        F={2, 4}  # accepting states
    )
    
    # todo: instantiate accordingly
    A0 = A.refuse()
        
    # todo: add appropriate test cases for A and A0
    test_words = ["aaa", "abb", "aab", "aba", "abb", "baa", "bab", "bba", "bbb"]
    
    print("Testing DFA A:")
    for word in test_words:
        print(f"{word}: {A.run(word)}")
    
    print("\nTesting DFA A0 (complement of A):")
    for word in test_words:
        print(f"{word}: {A0.run(word)}")


__main__()