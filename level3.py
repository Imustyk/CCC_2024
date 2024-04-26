import os


def is_valid_path(width, height, lawn, path):
    current_position = (0, 0)  # Initial position of the lawn mower
    visited = set()  # Set to store visited cells
    tree_position = None  # Position of the tree

    # Find the position of the tree
    for i in range(height):
        for j in range(width):
            if lawn[i][j] == 'X':
                tree_position = (i, j)
                break

    # Check if the initial position is on the tree
    if current_position == tree_position:
        return "INVALID"

    # Iterate through each move in the path
    for move in path:
        # Move the lawn mower according to the current move
        if move == 'S':
            current_position = (current_position[0] + 1, current_position[1])
        elif move == 'A':
            current_position = (current_position[0], current_position[1] - 1)
        elif move == 'W':
            current_position = (current_position[0] - 1, current_position[1])
        elif move == 'D':
            current_position = (current_position[0], current_position[1] + 1)

        # Check if the lawn mower goes out of bounds
        if current_position[0] < 0 or current_position[0] >= height or current_position[1] < 0 or current_position[1] >= width:
            return "INVALID"

        # Check if the lawn mower visits the tree
        if current_position == tree_position:
            return "INVALID"

        # Check if the lawn mower visits the same cell twice
        if current_position in visited:
            return "INVALID"

        # Add the current position to the set of visited cells
        visited.add(current_position)

    # Check if the lawn mower leaves the lawn after completing the path
    if current_position != tree_position:
        return "INVALID"

    # Check if all free cells are visited
    for i in range(height):
        for j in range(width):
            if lawn[i][j] == '.' and (i, j) not in visited:
                return "INVALID"

    # Check if the last cell is reached
    if current_position == (height - 1, width - 1):
        return "VALID"

    return "INVALID"


# Пример использования функции с чтением из файла
def read_lawn_mower_path(file_name):
    with open(file_name, 'r') as file:
        num_lawns = int(file.readline())
        results = []
        for _ in range(num_lawns):
            width, height = map(int, file.readline().split())
            lawn = [file.readline().strip() for _ in range(height)]
            path = file.readline().strip()
            results.append(is_valid_path(width, height, lawn, path))
    return results

# Функция для чтения пути газонокосилки и описания лужайки из файла
def read_lawn_mower_path(file_name):
    with open(file_name, 'r') as file:
        num_tests = int(file.readline())
        results = []
        for _ in range(num_tests):
            width, height = map(int, file.readline().split())
            lawn = [file.readline().strip() for _ in range(height)]
            path = file.readline().strip()
            results.append(is_valid_path(width, height, lawn, path))
    return results

# Пути к файлам ввода и вывода
input_folder = 'input/level3'
output_folder = 'output/level3'

# Обработка каждого входного файла и запись выходного файла
for file_name in os.listdir(input_folder):
    if file_name.endswith('.in'):
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name.replace('.in', '.out'))
        results = read_lawn_mower_path(input_path)
        with open(output_path, 'w') as file:
            for result in results:
                file.write(result + '\n')

print("Output files have been written to the output folder.")
