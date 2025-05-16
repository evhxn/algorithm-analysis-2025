---------------------------------PA2: Sudoku SAT Solver------------------------------------*
 Ethan Tapia  
 2400507  
 etapia@chapman.edu  
 CPSC 406 – Section 2
 
    **Running the code**  
      1. Change into the Sudoku directory:  
         cd Sudoku

      2. Run the SAT solver’s self‐test (four CNF examples):  
         python sat_solver.py

      3. Solve all five rubric Sudoku puzzles:  
         python sudoku_solver.py

        **Collaborators: 
           # Zach Ruhl (zruhl@chapman.edu)

-------------------------------------------------------------------------*  
    **Files / Classes:**  
    - sat_solver.py  
      • DPLL‐style SAT solver with unit propagation, clause filtering,  
        and total‐model construction.  
    - sudoku_solver.py  
      • Encodes a 9×9 Sudoku as CNF, invokes `sat_solve`, and decodes  
        the resulting Boolean model into a completed grid.  

    **Notes:**  
    - The SAT solver branches on the smallest unassigned variable ID,  
      trying True before False—this yields the *lexicographically* smallest  
      solution for under-constrained puzzles (so Puzzle 2 matches the hand-out  
      example exactly).  
    - All demo prints are behind `if __name__ == "__main__"` guards, so  
      importing the modules produces no output (required by the autograder).  

    **Resources:**  
    - “Understanding SAT by Implementing a Simple SAT Solver in Python”  
    - “Lecture Notes on SAT Solvers & DPLL” (CMU course notes)  
    - Nordström, J., “Introduction to Boolean Satisfiability”  
    - “Solving Sudoku with SAT” (Aalto University tutorial)  
    - “Optimized CNF Encoding for Sudoku Puzzles” (CMU hand-out)  
    - “Handling Python’s Recursion Limit” (GeeksforGeeks)  
    - “A Survey of SAT Solver Architecture” (heuristics & CDCL)  
    - “Boolean Satisfiability: Theory and Engineering” (CACM overview)  
    - Z3 Theorem Prover (Python API) — an SMT alternative  
    - PyEDA — Python library for Boolean algebra & SAT  

    |*/ Example output                      
      % python sat_solver.py  
      [[1, 2], [-1], [-2], [-1, -2]] → None  
      [[1, 2], [-1], [2]]            → {1: False, 2: True}  
      [[1], [2], [3], [-4], [-5], [-6]] → {1: True, 2: True, 3: True, 4: False, 5: False, 6: False}  
      [[1, -2], [-1, 2], [3], [-3, 4], [-4]] → None  

      % python sudoku_solver.py  
      Puzzle 1 → Solved  
      [5, 3, 4, 6, 7, 8, 9, 1, 2]  
      [6, 7, 2, 1, 9, 5, 3, 4, 8]  
      …  
      Puzzle 2 → Solved  
      [4, 5, 6, 7, 8, 1, 2, 9, 3]  
      [1, 2, 3, 4, 5, 9, 6, 7, 8]  
      …  
      Puzzle 3 → None  
      Puzzle 4 → None  
      Puzzle 5 → None  
-------------------------------------------------------------------------*  
#end
