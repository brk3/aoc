
def get_removals():
    # northwest, north, northeast, west, east, southwest, south, southeast
    positions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    can_remove = []

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '@' and (row, col) not in removed:
                adjacent_count = 0
                for dr, dc in positions:
                    r, c = row + dr, col + dc
                    if (0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == '@'
                            and (r, c) not in removed):
                        adjacent_count += 1

                if adjacent_count < 4:
                    can_remove.append((row, col))
    return can_remove

with open('input', 'r') as f:
    grid = [list(line.strip()) for line in f]

removed = []
removals = get_removals()
removed = removals

# TODO(pbourke): optimise to only check cells that have changed!
while len(removals) > 0:
    removals = get_removals()
    removed.extend(removals)
    print(len(removed))
