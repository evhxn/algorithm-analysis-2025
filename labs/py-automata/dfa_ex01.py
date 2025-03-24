import nfa

def __main__():
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
            (0, '0'): {0, 1},
            (0, '1'): {0},
            (1, '1'): {2},
            (2, '0'): {2},
            (2, '1'): {2}
        },
        q0=0,
        F={2}
    )

    # A4: NFA that accepts strings with a '1' in the 4th position
    A4 = nfa.NFA(
        Q={0, 1, 2, 3, 4},
        Sigma={'0', '1'},
        delta={
            (0, '0'): {1},
            (0, '1'): {1},
            (1, '0'): {2},
            (1, '1'): {2},
            (2, '0'): {3},
            (2, '1'): {3},
            (3, '1'): {4},
            (4, '0'): {4},
            (4, '1'): {4}
        },
        q0=0,
        F={4}
    )

    # Test words
    test_words = [
        "",        # empty string
        "0",       # single symbol
        "1", 
        "00",      # two symbols
        "01",
        "10", 
        "11",
        "000",     # three symbols
        "001",
        "010",
        "011",
        "100",
        "101", 
        "110",
        "111",
        "0000",    # four symbols
        "0001",
        "0010",
        "0011",
        "0100",
        "0101",
        "0110",
        "0111",
        "1000",
        "1001",
        "1010",
        "1011",
        "1100",
        "1101", 
        "1110",
        "1111"
    ]

    # Test each automaton
    automata = [A1, A2, A3, A4]
    for i, A in enumerate(automata, start=1):
        print(f"--- Testing A{i} ---")
        print(f"States: {A.Q}")
        print(f"Alphabet: {A.Sigma}")
        print(f"Initial State: {A.q0}")
        print(f"Final States: {A.F}")
        print("Transitions:")
        for (state, symbol), next_states in A.delta.items():
            print(f"  δ({state}, {symbol}) = {next_states}")
        print("Test Results:")
        for w in test_words:
            result = A.run(w)
            print(f"  '{w}': {result}")
        print()

if __name__ == "__main__":
    __main__()