import dfa
import nfa

def __main__():
    print("Exercise 2: DFA -> NFA")

    # Example DFA #1
    D1 = dfa.DFA(
        Q={0, 1},
        Sigma={'0', '1'},
        delta={
            (0, '0'): 0,
            (0, '1'): 1,
            (1, '0'): 0,
            (1, '1'): 1
        },
        q0=0,
        F={1}
    )
    # Convert to NFA
    N1 = D1.to_NFA()
    print("DFA D1:", D1)
    print("NFA N1 (from D1):", N1)
    words = ["", "0", "1", "00", "01", "10", "11", "111"]
    for w in words:
        print(f"D1.run({w}) = {D1.run(w)}, N1.run({w}) = {N1.run(w)}")
    print()

    print("Another DFA -> NFA")
    # Example DFA #2
    D2 = dfa.DFA(
        Q={0, 1, 2},
        Sigma={'0', '1'},
        delta={
            (0, '0'): 1,
            (0, '1'): 0,
            (1, '0'): 2,
            (1, '1'): 1,
            (2, '0'): 2,
            (2, '1'): 2
        },
        q0=0,
        F={2}
    )
    N2 = D2.to_NFA()
    print("DFA D2:", D2)
    print("NFA N2 (from D2):", N2)
    for w in words:
        print(f"D2.run({w}) = {D2.run(w)}, N2.run({w}) = {N2.run(w)}")
    print()

if __name__ == "__main__":
    __main__()