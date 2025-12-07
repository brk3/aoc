
with open('input', 'r') as f:
    grid = [list(line.strip()) for line in f]

count = 0
# northwest, north, northeast, west, east, southwest, south, southeast
positions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == '@':
            adjacent_count = 0
            for dr, dc in positions:
                r, c = row + dr, col + dc
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == '@':
                    adjacent_count += 1

            if adjacent_count < 4:
                count += 1

print(count)
