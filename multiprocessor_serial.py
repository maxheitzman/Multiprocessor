#built in python module

import argparse

# PHASE 1 – Serial Computation

# Stage 1.3.1 – Symbols
# Define the score value for each cell type
char_to_score = {
    'O': 3,   # Healthy O
    'o': 1,   # Weakened o
    '.': 0,   # Dead
    'x': -1,  # Weakened x
    'X': -3   # Healthy X
}

# Stage 1.3.2 – Iterative Rules
# Check if a number is in the Fibonacci sequence
def is_fibonacci(n):
    if n < 0: return False
    a, b = 0, 1
    while b < n: a, b = b, a + b
    return n == a or n == b

# Check if a number is prime
def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0: return False
    return True

# Check if a number is a power of two
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Stage 1.2.1 – Reading the Matrix File
# Reads the initial matrix from the file provided by -i
def read_matrix(path):
    with open(path, 'r') as f:
        return [list(line.strip()) for line in f if line.strip()]

# Stage 1.2.2 – Writing the Matrix File
# Writes the final matrix to the file specified by -o
def write_matrix(matrix, path):
    with open(path, 'w') as f:
        for row in matrix:
            f.write(''.join(row) + '\n')

# Stage 1.3 – Matrix Processing
# Calculates the sum of all 8 neighbors with wraparound
def neigh_count_sum(matrix, r, c):
    rows, cols = len(matrix), len(matrix[0])
    s = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = (r + dr) % rows, (c + dc) % cols
            s += char_to_score.get(matrix[nr][nc], 0)
    return s

# Applies the rules to each cell to compute the next generation
def next_state(matrix):
    rows, cols = len(matrix), len(matrix[0])
    new = [['.' for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            cell = matrix[r][c]
            score = neigh_count_sum(matrix, r, c)

            if cell == 'O':
                if is_fibonacci(score): new[r][c] = '.'
                elif score < 12: new[r][c] = 'o'
                else: new[r][c] = 'O'
            elif cell == 'o':
                if score < 0: new[r][c] = '.'
                elif score > 6: new[r][c] = 'O'
                else: new[r][c] = 'o'
            elif cell == '.':
                if is_power_of_two(score): new[r][c] = 'o'
                elif is_power_of_two(abs(score)): new[r][c] = 'x'
                else: new[r][c] = '.'
            elif cell == 'x':
                if score >= 1: new[r][c] = '.'
                elif score < -6: new[r][c] = 'X'
                else: new[r][c] = 'x'
            elif cell == 'X':
                if is_prime(abs(score)): new[r][c] = '.'
                elif score > -12: new[r][c] = 'x'
                else: new[r][c] = 'X'
    return new

# Stage 1.1 – Data Retrieval
# Entry point that parses arguments and runs the simulation
def main():
    print("Project :: R11626572")
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", required=True)  # Input file
    parser.add_argument("-o", required=True)  # Output file
    args = parser.parse_args()

    matrix = read_matrix(args.i)

    # Stage 1.3 – Run 100 iterations of the simulation
    for _ in range(100):
        matrix = next_state(matrix)

    # Stage 1.2.2 – Save the final output
    write_matrix(matrix, args.o)

if __name__ == "__main__":
    main()
