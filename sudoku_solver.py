"""
sudoku_solver.py  ––  uses sat_solver.sat_solve to crack 9×9 Sudokus.

Main entry point
----------------
sudoku_solve(grid)  →  solved grid    |    None (if unsatisfiable)

The `__main__` block at the bottom runs the **five puzzles** specified in the
PA-2 rubric, so you can verify behaviour quickly:

    $ python sudoku_solver.py
    Puzzle 1 …  Solved
    Puzzle 2 …  Solved
    Puzzle 3 …  None
    Puzzle 4 …  None
    Puzzle 5 …  None
"""

from typing import List
from sat_solver import sat_solve


# ────────────────── encoding helpers ──────────────────
def _var(i: int, j: int, d: int) -> int:
    """Bijective map  cell(i,j)=d   →   positive int 1‥729."""
    return 81 * (i - 1) + 9 * (j - 1) + d


def _exactly_one(lits):
    """CNF clauses enforcing ‘exactly one of these literals is true’."""
    yield lits                                   # at least one
    n = len(lits)
    for a in range(n):
        for b in range(a + 1, n):
            yield [-lits[a], -lits[b]]           # at most one


# ────────────────── CNF builder ───────────────────────
def sudoku_encode(grid: List[List[int]]):
    cls = []

    # 1. each cell exactly one digit
    for i in range(1, 10):
        for j in range(1, 10):
            cls += list(_exactly_one([_var(i, j, d) for d in range(1, 10)]))

    # 2. row uniqueness
    for i in range(1, 10):
        for d in range(1, 10):
            cls += list(_exactly_one([_var(i, j, d) for j in range(1, 10)]))

    # 3. column uniqueness
    for j in range(1, 10):
        for d in range(1, 10):
            cls += list(_exactly_one([_var(i, j, d) for i in range(1, 10)]))

    # 4. 3×3 box uniqueness
    for bi in range(0, 3):
        for bj in range(0, 3):
            for d in range(1, 10):
                lits = [
                    _var(i, j, d)
                    for i in range(1 + 3 * bi, 4 + 3 * bi)
                    for j in range(1 + 3 * bj, 4 + 3 * bj)
                ]
                cls += list(_exactly_one(lits))

    # 5. clues
    for i in range(9):
        for j in range(9):
            if grid[i][j]:
                cls.append([_var(i + 1, j + 1, grid[i][j])])

    return cls


# ────────────────── public solver ─────────────────────
def sudoku_solve(grid: List[List[int]]):
    model = sat_solve(sudoku_encode(grid))
    if model is None:
        return None

    solved = [[0] * 9 for _ in range(9)]
    for i in range(1, 10):
        for j in range(1, 10):
            for d in range(1, 10):
                if model[_var(i, j, d)]:
                    solved[i - 1][j - 1] = d
                    break
    return solved


# ────────────────── demo puzzles (rubric) ─────────────
if __name__ == "__main__":
    puzzles = [
        # Puzzle 1 – solvable
        [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ],
        # Puzzle 2 – solvable (all zeros except three clues)
        [
            [0, 0, 0, 0, 0, 1, 2, 0, 3],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ],
        # Puzzle 3 – duplicate ‘1’ in first row → unsat
        [
            [1, 1, 0, 0, 0, 0, 0, 0, 0],
            *[[0] * 9 for _ in range(8)],
        ],
        # Puzzle 4 – diagonal ones → unsat
        [
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1],
        ],
        # Puzzle 5 – nearly full but inconsistent → unsat
        [
            [5, 1, 6, 8, 4, 9, 7, 3, 2],
            [3, 0, 7, 6, 0, 5, 0, 0, 0],
            [8, 0, 9, 7, 0, 0, 0, 6, 5],
            [1, 3, 5, 0, 6, 0, 9, 0, 7],
            [4, 7, 2, 5, 9, 1, 0, 0, 6],
            [9, 6, 8, 3, 7, 0, 0, 5, 0],
            [2, 5, 3, 1, 8, 6, 0, 7, 4],
            [6, 8, 4, 2, 0, 7, 5, 0, 0],
            [7, 9, 1, 0, 5, 0, 6, 0, 8],
        ],
    ]

    for idx, puzzle in enumerate(puzzles, 1):
        result = sudoku_solve(puzzle)
        status = "Solved" if result else "None"
        print(f"Puzzle {idx} → {status}")
        if result:
            for row in result:
                print(row)
        print()
# ──────────────────────────────────────────────────────────────────────────