from itertools import combinations
from collections import defaultdict

def get_antinode_pos(a, b, seen):
    row_a, col_a = a
    row_b, col_b = b

    row_diff = row_b - row_a
    col_diff = col_b - col_a

    seen.add((row_a, col_a))
    seen.add((row_b, col_b))

    # top diagonal
    i, j = (row_a - row_diff, col_a - col_diff)
    while (i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0])):
        seen.add((i, j))
        i -= row_diff
        j -= col_diff

    # bottom
    i, j = (row_b + row_diff, col_b + col_diff)
    while (i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0])):
        seen.add((i, j))
        i += row_diff
        j += col_diff

with open('input', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

matrix = []
antennas = defaultdict(list)
for i in range(len(lines)):
    line = []
    for j in range(len(lines[0])):
        line.append(lines[i][j])
        if lines[i][j] != '.':
            antennas[lines[i][j]].append((i, j))
    matrix.append(line)

seen = set()
for antennas, positions in antennas.items():
    for pos_a, pos_b in combinations(positions, 2):
        # seen.add((pos_a, pos_b))
        get_antinode_pos(pos_a, pos_b, seen)

print(len(seen))
