# Multiprocessor Cellular Automaton Simulator

This project implements a two-phase simulation of cellular behavior based on a modified set of rules inspired by Conway’s Game of Life. It includes both a serial and a concurrent (multiprocessing) implementation written in Python.

---

## Features

- Handles 100 iterations of a cellular matrix simulation  
- Phase 1: Serial computation of matrix state evolution  
- Phase 2: Parallel computation using Python’s multiprocessing module  
- Accepts flexible command-line arguments for input/output and number of processes  
- Supports wrap-around neighbor calculation  

---

## Symbols and Cell States

Each character in the input matrix represents a cell state:

- O – Healthy O Cell (+3)  
- o – Weakened O Cell (+1)  
- X – Healthy X Cell (-3)  
- x – Weakened X Cell (-1)  
- . – Dead Cell (0)  

The simulation evolves based on neighbor scoring and logic related to:
- Fibonacci sequences  
- Prime numbers  
- Powers of two  

---

## How to Run

Example usage:

    python3 Multiprocessor.py -i six_by_six_v2/time_step_0.dat -o six_by_six_v2/time_step_100.dat -p 4

### Command-Line Arguments:

- `-i <input_file>`: Required. Input matrix file path  
- `-o <output_file>`: Required. Output file to write the final matrix  
- `-p <process_count>`: Optional. Number of parallel processes (defaults to 1)  

---

## File Structure

    Multiprocessor/
    ├── Multiprocessor.py
    ├── README.md
    └── six_by_six_v2/
        ├── time_step_0.dat
        ├── time_step_1.dat
        ├── ...
        └── time_step_100.dat (generated)

---

## Output

- First line printed to terminal:

      Project :: R11626572

- Output file will contain the final matrix after 100 iterations  
- The output format must match the input:
  - No extra spacing  
  - One row per line  
  - Characters only (O, o, X, x, or .)  

---

## Notes

- Wrapping is supported: cells at the edge wrap around and always have 8 neighbors  
- Only standard Python libraries are used — no external dependencies  
- Includes helper functions for:
  - Fibonacci detection  
  - Prime number check  
  - Power of two check  

---

## Requirements

- Python 3.13+  
- Unix-like terminal or IDE that supports command-line arguments  
