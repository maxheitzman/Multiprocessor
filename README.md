# Multiprocessor Cellular Automaton Simulator

This project implements a two-phase simulation of cellular behavior based on a modified set of rules inspired by Conway’s Game of Life. It includes both a serial and a concurrent (multiprocessing) implementation written in Python.

---

## Versions

- `Multiprocessor.py` – Final version using multiprocessing for parallel computation
- `multiprocessor_serial.py` – Phase 1: serial-only version used to test and validate matrix evolution rules

---

## Features

- Simulates 100 iterations of a symbolic matrix
- Serial and parallel versions available
- Accepts command-line arguments for input, output, and process count
- Wrap-around logic for neighbor detection (toroidal grid)
- Rule logic based on:
  - Fibonacci numbers
  - Prime numbers
  - Powers of two

---

## Symbols and Cell States

Each cell is represented by a character:

- `O` – Healthy O Cell (+3)  
- `o` – Weakened O Cell (+1)  
- `X` – Healthy X Cell (-3)  
- `x` – Weakened X Cell (-1)  
- `.` – Dead Cell (0)

---

## How to Run

Example (parallel version):

```
python3 Multiprocessor.py -i six_by_six_part1/time_step_0.dat -o six_by_six_part2/time_step_100.dat -p 4
```

Example (serial version):

```
python3 multiprocessor_serial.py -i six_by_six_part1/time_step_0.dat -o six_by_six_part2/time_step_100.dat
```

### Command-Line Arguments

- `-i <input_file>`: Required. Path to input `.dat` file  
- `-o <output_file>`: Required. Path to output `.dat` file  
- `-p <process_count>`: Optional. Number of processes (defaults to 1 in parallel version)

---

## File Structure

```
Multiprocessor/
├── Multiprocessor.py
├── multiprocessor_serial.py
├── README.md
├── six_by_six_part1/
│   ├── time_step_0.dat
│   ├── ...
│   └── time_step_49.dat
└── six_by_six_part2/
    ├── time_step_50.dat
    ├── ...
    └── time_step_100.dat
```

---

## Output Format

- Console output always begins with:

  ```
  Project :: R11626572
  ```

- Output file contains the matrix after 100 iterations  
- Output must match input formatting:
  - One row per line
  - No extra whitespace
  - Only cell characters (O, o, X, x, .)

---

## Notes

- Wrapping is applied in all directions (toroidal grid)
- The simulator uses only built-in Python libraries
- Includes helper functions for:
  - Fibonacci detection
  - Prime number check
  - Power of two detection

---

## Requirements

- Python 3.13 or later  
- Terminal or IDE that supports command-line execution

---

## Requirements

- Python 3.13 or later
- Terminal or IDE that supports command-line arguments

