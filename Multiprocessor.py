#Max Heitzman 
#Phase 2: Parallel Computation

import argparse
import os
import multiprocessing

#Used From Phase 1 - Argument Parsing and Validation

def check_input_file(file_path):
    if not os.path.isfile(file_path):
        raise argparse.ArgumentTypeError(f"INPUT FILE AINT IT or dont excist {file_path}")
    return file_path

def check_output_file(file_path):
    folder = os.path.dirname(file_path) or '.'
    if not os.path.isdir(folder):
        raise argparse.ArgumentTypeError(f"Output FIle AINT IT or dont exist {folder}")
    return file_path

def get_args():
    parser = argparse.ArgumentParser(description="Cellular automaton simulator (parallel version)")
    parser.add_argument("-i", "--input", type=check_input_file, required=True, help="Input matrix file")
    parser.add_argument("-o", "--output", type=check_output_file, required=True, help="Where to save output")
    parser.add_argument("-p", "--processes", type=int, default=1, help="Number of processes")
    return parser.parse_args()

#Used From Phase 1 - Matrix File I/O

def load_matrix(filename):
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f if line.strip()]

def save_matrix(matrix, filename):
    with open(filename, 'w') as f:
        for row in matrix:
            f.write(''.join(row) + '\n')

#Used From Phase 1 - Helper Functions

score_value = {
    'O': 3,
    'o': 1,
    '.': 0,
    'x': -1,
    'X': -3
}

def neighbor_total(matrix, r, c):
    total = 0
    height = len(matrix)
    width = len(matrix[0])
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr = (r + dr) % height
            nc = (c + dc) % width
            total += score_value.get(matrix[nr][nc], 0)
    return total

def is_fibonacci(n):
    if n < 0:
        return False
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return n == a or n == b

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_pow2(n):
    return n > 0 and (n & (n - 1)) == 0

#Phase 2 - Stage 2.1: Parallel Chunk Processing

#fucntion that runs a single process and handles a chunk of rows
#aplies simulation rules to the assigned rows
def simulate_step_chunk(rows, matrix, start_row, result_queue):
    updated = [] #will store upadted rows of the chunk

    for i, row in enumerate(rows): #loops through each row in the current chunk
        r = start_row + i #gets the row index in the full matrix
        new_row = [] #stores upadated symbols for this row

        for c in range(len(row)): #loops through each cell in the row
            symbol = matrix[r][c] #current symbol at the postion of [r][c]
            score = neighbor_total(matrix, r, c) #calculates the sum of the neighbor values

            if symbol == 'O':
                if is_fibonacci(score):
                    new_row.append('.')
                elif score < 12:
                    new_row.append('o')
                else:
                    new_row.append('O')

            elif symbol == 'o':
                if score < 0:
                    new_row.append('.')
                elif score > 6:
                    new_row.append('O')
                else:
                    new_row.append('o')

            elif symbol == '.':
                if is_pow2(score):
                    new_row.append('o')
                elif is_pow2(abs(score)):
                    new_row.append('x')
                else:
                    new_row.append('.')

            elif symbol == 'x':
                if score >= 1:
                    new_row.append('.')
                elif score < -6:
                    new_row.append('X')
                else:
                    new_row.append('x')

            elif symbol == 'X':
                if is_prime(abs(score)):
                    new_row.append('.')
                elif score > -12:
                    new_row.append('x')
                else:
                    new_row.append('X')

        updated.append(new_row) #adds the updated row to the result list

#sends thre upadted chunk of rows and their starting row index back to the main process
    result_queue.put((start_row, updated))

#Phase 2 - Stage 2.2: Main Entry Point With Multiprocessing

def main():
    print("Project :: R11626572")

    args = get_args() #parses command line arguments
    matrix = load_matrix(args.input) #loads the starting matrix from the input file
    num_processes = max(1, args.processes) #makes sure atleast 1 process
    height = len(matrix) #rows in the matrix

    for _ in range(100): #run 100 interations like desbirbed 
        chunk_size = height // num_processes #calculates # of rows per process
        result_queue = multiprocessing.Queue() #stalls kinda or queues which gathers results from processes
        processes = [] #stores all the running processes

        for i in range(num_processes): #gets one process per chunk (if -p 4 it will loop 4 times for 4 chunks and 4 processes)
            start_row = i * chunk_size 
            end_row = height if i == num_processes - 1 else (i + 1) * chunk_size #last proccess get all remaing rows in case 100 isnt divisble evenly
            chunk = matrix[start_row:end_row] #slices the matrix for the proccess

            #new process that runs the simulate_step_chunk()
            p = multiprocessing.Process( 
                target=simulate_step_chunk,
                args=(chunk, matrix, start_row, result_queue)
                ) 
            #chunk->only rows this process will be updated
            #matrix->full matrix needed for the neighbors
            #start_row->so the process places the result to here
            #result_queue-> so the last proccess or like child can send its results back
            p.start() 
            processes.append(p) #stores the porocess object in a list 

        new_matrix = [None] * height #temporary place for the updated matrix to be stored
        for _ in range(num_processes): #get the updated rows from all processes
            start_row, updated_rows = result_queue.get()
            new_matrix[start_row:start_row + len(updated_rows)] = updated_rows

        for p in processes: #waits for all proccesses to finish
            p.join()

        matrix = new_matrix #replaces old matrix with the new upadted one for the next iteration

    save_matrix(matrix, args.output) #saves the final matrix to the output file

if __name__ == "__main__":
    main()
