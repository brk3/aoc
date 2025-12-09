
grid = []

with open('input', 'r') as f:
    lines = f.readlines()
    for line in lines[:-1]:
        grid.append(list(map(int, line.strip().split())))
    operators = lines[-1].split()

ans = 0

for i in range(len(operators)):
    cur = grid[0][i]
    for j in range(1, len(grid)):
        if operators[i] == '+':
            cur += grid[j][i]
        else:
            cur *= grid[j][i]
    ans += cur

print(ans)
