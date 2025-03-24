# a class for DFAs
# modified as needed
# dfa.py

import nfa

class DFA:
    def __init__(self, Q, Sigma, delta, q0, F):
        """
        Q     : set of states
        Sigma : set of symbols
        delta : dict((state, symbol) -> next_state)
        q0    : initial state
        F     : set of accepting states
        """
        self.Q = Q
        self.Sigma = Sigma
        self.delta = delta
        self.q0 = q0
        self.F = F

    def __repr__(self):
        return (
            f"DFA(\n"
            f"  Q={self.Q},\n"
            f"  Sigma={self.Sigma},\n"
            f"  delta={self.delta},\n"
            f"  q0={self.q0},\n"
            f"  F={self.F}\n"
            f")"
        )

    def run(self, w):
        """Return True if w is accepted by this DFA, False otherwise."""
        current_state = self.q0
        for symbol in w:
            if (current_state, symbol) in self.delta:
                current_state = self.delta[(current_state, symbol)]
            else:
                return False
        return current_state in self.F

    def to_NFA(self):
        """
        Construct an NFA from this DFA in the 'natural' way:
          - same set of states Q
          - for each (q,a), define delta_NFA(q,a) = {delta_DFA(q,a)}
          - same initial and final states
        """
        new_delta = {}
        for (q, a), nxt in self.delta.items():
            new_delta[(q, a)] = {nxt}
        return nfa.NFA(self.Q, self.Sigma, new_delta, self.q0, self.F)
        
    def refuse(self):
        """
        Returns a new DFA that is the complement of this DFA.
        It accepts exactly those strings that this DFA rejects.
        """
        # Create a copy with the accepting states complemented
        return DFA(
            Q=self.Q,
            Sigma=self.Sigma,
            delta=self.delta.copy(),
            q0=self.q0,
            F=self.Q - self.F  # Complement of accepting states
        )
        
    def both(self, other):
        """
        Returns a new DFA that is the intersection of this DFA and other DFA.
        It accepts exactly those strings that are accepted by both DFAs.
        
        The states of the new DFA are pairs (q1, q2) where q1 is a state of self
        and q2 is a state of other.
        """
        # Check if alphabets are compatible
        if self.Sigma != other.Sigma:
            raise ValueError("The two DFAs must have the same alphabet")
        
        # Product construction
        # States are pairs (q1, q2)
        Q_product = {(q1, q2) for q1 in self.Q for q2 in other.Q}
        q0_product = (self.q0, other.q0)
        F_product = {(q1, q2) for q1 in self.F for q2 in other.F}
        
        # Transition function
        delta_product = {}
        for q1 in self.Q:
            for q2 in other.Q:
                for symbol in self.Sigma:
                    if (q1, symbol) in self.delta and (q2, symbol) in other.delta:
                        delta_product[((q1, q2), symbol)] = (self.delta[(q1, symbol)], other.delta[(q2, symbol)])
        
        # Create and return the product DFA
        return DFA(
            Q=Q_product,
            Sigma=self.Sigma,
            delta=delta_product,
            q0=q0_product,
            F=F_product
        )