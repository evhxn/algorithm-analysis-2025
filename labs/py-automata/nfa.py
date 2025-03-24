import dfa
from collections import deque

class NFA:
    def __init__(self, Q, Sigma, delta, q0, F):
        """
        Q     : set of states (e.g. {0,1,2})
        Sigma : set of symbols (e.g. {'0','1'})
        delta : dict((state, symbol) -> set_of_next_states)
        q0    : initial state (e.g. 0)
        F     : set of accepting states (e.g. {2})
        """
        self.Q = Q
        self.Sigma = Sigma
        self.delta = delta
        self.q0 = q0
        self.F = F

    def __repr__(self):
        return (
            f"NFA(\n"
            f"  Q={self.Q},\n"
            f"  Sigma={self.Sigma},\n"
            f"  delta={self.delta},\n"
            f"  q0={self.q0},\n"
            f"  F={self.F}\n"
            f")"
        )

    def run(self, w):
        current_states = {self.q0}
        for symbol in w:
            next_states = set()
            for state in current_states:
                if (state, symbol) in self.delta:
                    next_states |= self.delta[(state, symbol)]
            current_states = next_states
            if not current_states:
                break
        return len(current_states & self.F) > 0

    def to_DFA(self):
        from_state = lambda s: frozenset(s) if isinstance(s, set) else frozenset([s])

        start_subset = from_state(self.q0)
        # BFS/queue over subsets
        queue = deque([start_subset])
        dfa_states = {start_subset}
        dfa_delta = {}
        dfa_accepting = set()

        # If start_subset intersects F, mark it accepting
        if start_subset & self.F:
            dfa_accepting.add(start_subset)

        while queue:
            subset = queue.popleft()
            for symbol in self.Sigma:
                next_subset = set()
                for s in subset:
                    if (s, symbol) in self.delta:
                        next_subset |= self.delta[(s, symbol)]
                if next_subset:
                    fs = frozenset(next_subset)
                    dfa_delta[(subset, symbol)] = fs
                    if fs not in dfa_states:
                        dfa_states.add(fs)
                        queue.append(fs)
                        if fs & self.F:
                            dfa_accepting.add(fs)
                else:
                    # No next state => so no "dead" state
                    pass

        return dfa.DFA(
            Q=dfa_states,
            Sigma=self.Sigma,
            delta=dfa_delta,
            q0=start_subset,
            F=dfa_accepting
        )