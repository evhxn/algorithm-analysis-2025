import nfa
import dfa

def __main__():
    print("=== Exercise 3: NFA -> DFA (Determinization) ===")
    
    # A1: NFA that accepts strings that end with '1'
    A1 = nfa.NFA(
        Q={0, 1},
        Sigma={'0', '1'},
        delta={
            (0, '0'): {0},
            (0, '1'): {1},
            (1, '0'): {0},
            (1, '1'): {1}
        },
        q0=0,
        F={1}
    )

    # A2: NFA that accepts strings with length at least 2
    A2 = nfa.NFA(
        Q={0, 1, 2},
        Sigma={'0', '1'},
        delta={
            (0, '0'): {1},
            (0, '1'): {1},
            (1, '0'): {2},
            (1, '1'): {2},
            (2, '0'): {2},
            (2, '1'): {2}
        },
        q0=0,
        F={2}
    )

    # A3: NFA that accepts strings with pattern '01'
    A3 = nfa.NFA(
        Q={0, 1, 2},
        Sigma={'0', '1'},
        delta={
            (0, '0'): {1},
            (0, '1'): {0},
            (1, '1'): {2},
            (2, '0'): {2},
            (2, '1'): {2}
        },
        q0=0,
        F={2}
    )

    # A4: NFA with nondeterministic transitions
    A4 = nfa.NFA(
        Q={0, 1, 2, 3},
        Sigma={'0', '1'},
        delta={
            (0, '0'): {0, 1},
            (0, '1'): {0, 2},
            (1, '0'): {3},
            (1, '1'): {},
            (2, '0'): {},
            (2, '1'): {3},
            (3, '0'): {3},
            (3, '1'): {3}
        },
        q0=0,
        F={3}
    )
    
    nfa_list = [A1, A2, A3, A4]
    
    # Test words
    test_words = ["", "0", "1", "00", "01", "10", "11", "000", "010", "101", "111"]
    
    # Determinize each NFA and test
    for i, N in enumerate(nfa_list, start=1):
        print(f"\n--- Determinizing A{i} ---")
        print("Original NFA:")
        print(N)
        
        # Convert to DFA
        D = N.to_DFA()
        print("\nResulting DFA:")
        print(D)
        
        # Test both with the same inputs
        print("\nTest Results:")
        for w in test_words:
            nfa_result = N.run(w)
            dfa_result = D.run(w)
            match = "✓" if nfa_result == dfa_result else "✗"
            print(f"  '{w}': NFA: {nfa_result}, DFA: {dfa_result} {match}")
        
        # Analyze the resulting DFA
        print("\nObservations:")
        print(f"The original NFA had {len(N.Q)} states")
        print(f"The resulting DFA has {len(D.Q)} states")
        print(f"The DFA states represent these subsets of NFA states:")
        for dfa_state in D.Q:
            print(f"  {dfa_state}")

if __name__ == "__main__":
    __main__()