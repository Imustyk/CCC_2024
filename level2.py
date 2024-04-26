import os
from utils import read_file, write_solution


# Modify the create_df function to split paths by newline characters
def create_df(file_in):
    tokens = file_in.strip().split('\n')
    num_paths = int(tokens[0])  # Extract the number of paths
    paths = tokens[1:]  # Extract paths
    return paths


# Define a function to calculate the size of the smallest rectangular lawn
def calculate_lawn_size(path):
    # Initialize minimum and maximum coordinates
    min_x = min_y = max_x = max_y = 0

    # Track current position
    x = y = 0

    # Update minimum and maximum coordinates based on each move
    for move in path:
        if move == 'W':
            y += 1
        elif move == 'D':
            x += 1
        elif move == 'S':
            y -= 1
        elif move == 'A':
            x -= 1

        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    # Calculate width and height of the rectangular lawn
    width = max_x - min_x + 1
    height = max_y - min_y + 1

    return width, height


# Define the solve_level2 function to calculate lawn sizes for all paths
def solve_level2(paths):
    lawn_sizes = []
    for path in paths:
        width, height = calculate_lawn_size(path)
        lawn_sizes.append((width, height))
    return lawn_sizes


if __name__ == '__main__':
    in_path = 'input/level2/'
    out_path = 'output/level2/'

    files = os.listdir(in_path)
    files = [f for f in files if f.endswith('.txt')]  # Adjust file extension filter
   # files = ['level2_5.in']
    for f in files:
        file_content = read_file(os.path.join(in_path, f))
        paths = create_df(file_content)
        solution = solve_level2(paths)
        solution_str = '\n'.join(' '.join(map(str, size)) for size in solution)
        print(solution_str)
        write_solution(os.path.join(out_path, f.replace('.txt', '.out')), solution_str)  # Adjust output file extension
