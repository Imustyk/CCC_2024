import os
from utils import read_file, write_solution


# Define the count_directions function
def count_directions(paths):
    counts = []
    for path in paths:
        # Create a dictionary to count occurrences of each direction
        counts_dict = {'W': 0, 'D': 0, 'S': 0, 'A': 0}

        # Count occurrences of each direction in the current path
        for char in path:
            if char in counts_dict:
                counts_dict[char] += 1

        # Append the counts as a list to the counts list
        counts.append(counts_dict.values())

    return counts


# Modify the create_df function to split paths by newline characters
def create_df(file_in):
    paths = file_in.strip().split('\n')[1:]  # Extract paths, skipping the first line
    return paths


# Modify the solve_level1 function to use count_directions
def solve_level1(paths):
    counts = count_directions(paths)
    # Join the counts for each path into a string, separated by space
    return '\n'.join(' '.join(map(str, count)) for count in counts)


if __name__ == '__main__':
    in_path = 'input/level1/'
    out_path = 'output/level1/'

    files = os.listdir(in_path)
    files = [f for f in files if f.endswith('.txt')]  # Adjust file extension filter
    #files = ['level1_5.in']
    for f in files:
        file_content = read_file(os.path.join(in_path, f))
        paths = create_df(file_content)
        solution = solve_level1(paths)
        print(solution)
        write_solution(os.path.join(out_path, f.replace('.txt', '.out')), solution)  # Adjust output file extension
