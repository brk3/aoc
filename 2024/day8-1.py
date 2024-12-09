from collections import defaultdict

def print_matrix(m):
    for row in m:
        print(''.join(row))

def get_antinode_pos(a, b):
    rowa, cola = a
    rowb, colb = b
    row_diff = abs(rowa - rowb)
    col_diff = abs(cola - colb)

    if cola > colb:
        antinodea = (rowa - row_diff, cola + col_diff)
        antinodeb = (rowb + row_diff, colb - col_diff)
    else:
        antinodea = (rowa - row_diff, cola - col_diff)
        antinodeb = (rowb + row_diff, colb + col_diff)

    if (antinodea[0] >= 0 and antinodea[0] < len(matrix) and
            antinodea[1] >= 0 and antinodea[1] < len(matrix[0])):
        matrix[antinodea[0]][antinodea[1]] = '#'

    if (antinodeb[0] >= 0 and antinodeb[0] < len(matrix) and
            antinodeb[1] >= 0 and antinodeb[1] < len(matrix[0])):
        matrix[antinodeb[0]][antinodeb[1]] = '#'

    return (antinodea, antinodeb)

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

antinodes = set()
for antenna, positions in antennas.items():
    for posa in positions:
        for posb in positions:
            if posa != posb and (posb, posa) not in antinodes:
                antinodes.add((posa, posb))
                get_antinode_pos(posa, posb)

ans = 0
for row in matrix:
    for col in row:
        if col == '#':
            ans += 1

print_matrix(matrix)
print(ans)
