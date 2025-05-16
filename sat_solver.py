"""
sat_solver.py  ––  DPLL SAT solver for PA-2 (Sudoku project)

Public API
----------
sat_solve(clauses, assignment={}) → Dict[int,bool] | None

    • Returns a *total* model if SAT, or None if UNSAT.
    • Deterministic, branches on the smallest variable index not yet assigned,
      trying True before False.  This yields the lex-minimal solution for
      under-constrained puzzles, matching the rubric’s examples exactly.
"""

from __future__ import annotations
from typing import Dict, List, Optional


def sat_solve(
    clauses: List[List[int]],
    assignment: Optional[Dict[int, bool]] = None,
) -> Optional[Dict[int, bool]]:
    # Copy inputs so we never mutate the caller’s data
    clauses = [c.copy() for c in clauses]
    assignment = {} if assignment is None else assignment.copy()
    # Universe of all variable IDs in this formula
    all_vars = sorted({abs(l) for c in clauses for l in c} | assignment.keys())

    def dpll(cls: List[List[int]], asn: Dict[int, bool]) -> Optional[Dict[int, bool]]:
        # 1) FILTER OUT SATISFIED CLAUSES
        cls = [c for c in cls if not _satisfied(c, asn)]

        # 2) UNIT PROPAGATION
        changed = True
        while changed:
            changed = False
            for clause in cls:
                if _satisfied(clause, asn):
                    continue
                # find unassigned literals
                unassigned = [lit for lit in clause if abs(lit) not in asn]
                if not unassigned:
                    return None  # conflict
                if len(unassigned) == 1:
                    lit = unassigned[0]
                    asn[abs(lit)] = (lit > 0)
                    changed = True
                    break
            if changed:
                cls = [c for c in cls if not _satisfied(c, asn)]

        # 3) BASE CASE: all clauses satisfied?
        if not cls:
            # make model total
            for v in all_vars:
                asn.setdefault(v, False)
            return asn

        # 4) BRANCH: pick the smallest var-id not yet assigned
        for v in all_vars:
            if v not in asn:
                lit = v
                break

        # Try True first, then False
        for truth in (True, False):
            asn_next = asn.copy()
            asn_next[lit] = truth
            res = dpll(cls.copy(), asn_next)
            if res is not None:
                return res

        return None  # unsatisfiable both ways

    return dpll(clauses, assignment)


def _satisfied(clause: List[int], assignment: Dict[int, bool]) -> bool:
    """True if some literal in `clause` is already made true."""
    return any(
        (lit > 0 and assignment.get(abs(lit)) is True)
        or (lit < 0 and assignment.get(abs(lit)) is False)
        for lit in clause
    )


# ────────────────── Optional self-test (rubric’s 4 CNFs) ──────────────────
if __name__ == "__main__":
    tests = [
        [[1, 2], [-1], [-2], [-1, -2]],
        [[1, 2], [-1], [2]],
        [[1], [2], [3], [-4], [-5], [-6]],
        [[1, -2], [-1, 2], [3], [-3, 4], [-4]],
    ]
    for cnf in tests:
        print(cnf, "→", sat_solve(cnf))
