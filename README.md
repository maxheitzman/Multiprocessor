# Multiprocessor Cellular Automaton Simulator

This project implements a two-phase simulation of cellular behavior based on a modified set of rules inspired by Conway’s Game of Life. It includes both a serial and a concurrent (multiprocessing) implementation written in Python.

---

## Features

- Simulates 100 iterations of a cellular automaton matrix
- Phase 1: Serial evolution logic
- Phase 2: Parallel logic using Python's multiprocessing module
- Accepts flexible command-line arguments for input, output, and core count
- Supports wrap-around edge behavior (toroidal matrix)

---

## Symbols and Cell States

Each symbol in the matrix represents a cell state:

- O – Healthy O Cell (+3)  
- o – Weakened O Cell (+1)  
- X – Healthy X Cell (-3)  
- x – Weakened X Cell (-1)  
- . – Dead Cell (0)  

Cell evolution depends on the sum of neighbor scores and their relationship to:
- Fibonacci numbers
- Prime numbers
- Powers of two

---

## How to Run

Basic usage:

    python3 Multiprocessor.py -i six_by_six_part1/time_step_0.dat -o six_by_six_part2/time_step_100.dat -p 4

### Command-Line Arguments

- `-i <input_file>`: Required — starting matrix file path  
- `-o <output_file>`: Required — output file to write after 100 iterations  
- `-p <process_count>`: Optional — number of parallel processes to use (default is 1)

---

## File Structure

    Multiprocessor/
    ├── Multiprocessor.py
    ├── README.md
    ├── six_by_six_part1/
    │   ├── time_step_0.dat
    │   ├── ...
    │   └── time_step_49.dat
    └── six_by_six_part2/
        ├── time_step_50.dat
        ├── ...
        └── time_step_100.dat (output)

---

## Output Format

- Terminal output:

      Project :: R11626572

- Output file will contain the final matrix after 100 iterations
- Format must match the input:
  - Each row on a new line
  - No added spacing or formatting
  - Only characters: O, o, X, x, or .

---

## Notes

- Cells wrap around at the edges (neighbors wrap)
- All logic is implemented using standard Python 3 libraries
- Includes helper checks for:
  - Fibonacci detection
  - Prime number detection
  - Power of two detection

---

## Requirements

- Python 3.13 or later
- Terminal or IDE that supports command-line arguments

