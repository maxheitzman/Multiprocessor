# Multiprocessor Cellular Automaton Simulator

This project implements a two-phase simulation of cellular behavior based on a modified set of rules inspired by Conway’s Game of Life. It includes both a serial and a concurrent (multiprocessing) implementation written in Python.

Features:

- Handles 100 iterations of a cellular matrix simulation
- Phase 1: Serial computation of matrix state evolution
- Phase 2: Parallel computation using Python’s multiprocessing module
- Accepts flexible command-line arguments for input/output and number of processes
- Supports wrap-around neighbor calculation

Symbols and Cell States:

O  – Healthy O Cell (+3)  
o  – Weakened O Cell (+1)  
X  – Healthy X Cell (-3)  
x  – Weakened X Cell (-1)  
.  – Dead Cell (0)

The simulation evolves based on neighbor scoring and logic related to:
- Fibonacci sequences
- Prime numbers
- Powers of two

How to Run:

Example:

python3 SyntaxParser.py -i six_by_six_v2/time_step_0.dat -o six_by_six_v2/time_step_100.dat -p 4

Command-Line Arguments:

- -i <input_file>: Required. Input matrix file path.  
- -o <output_file>: Required. Output file to write the final matrix.  
- -p <process_count>: Optional. Number of parallel processes. Defaults to 1.

File Structure:

Multiprocessor/
├── SyntaxParser.py  
├── README.md  
└── six_by_six_v2/  
  ├── time_step_0.dat  
  ├── ...  
  └── time_step_100.dat

Output:

- First line printed: Project :: R11626572
- Output file contains the matrix after 100 iterations
- Output format matches input: no extra spacing, just rows of characters

Notes:

- Wrapping is supported: cells at the edge wrap around to consider all 8 neighbors
- Only standard Python libraries are used — no external packages like NumPy
- Project includes helpers for Fibonacci, prime, and power-of-two detection

Requirements:

- Python 3.13+
- Unix-like terminal environment or IDE that supports arguments

