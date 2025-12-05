
grid = []

with open('input', 'r') as f:
    for line in f:
        entry = []
        grid.append([x for x in line.strip()])


N = len(grid[0])
M = len(grid)
count = 0

for row in range(M):
    for col in range(N):
        adjacent_count = 0
        if grid[row][col] == '@':
            # north
            if row > 0 and grid[row-1][col] == '@':
                adjacent_count += 1
            # north-east
            if row > 0 and col < N-1 and grid[row-1][col+1] == '@':
                adjacent_count += 1
            # east
            if col < N-1 and grid[row][col+1] == '@':
                adjacent_count += 1
            # south-east
            if col < N-1 and row < M-1 and grid[row+1][col+1] == '@':
                adjacent_count += 1
            # south
            if row < M-1 and grid[row+1][col] == '@':
                adjacent_count += 1
            # south-west
            if row < M-1 and col > 0 and grid[row+1][col-1] == '@':
                adjacent_count += 1
            # west
            if col > 0 and grid[row][col-1] == '@':
                adjacent_count += 1
            # north-west
            if row > 0 and col > 0 and grid[row-1][col-1] == '@':
                adjacent_count += 1

            if adjacent_count < 4:
                count += 1

print(count)
