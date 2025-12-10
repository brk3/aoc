import math

grid = []

with open('input', 'r') as f:
    lines = f.readlines()
    grid = [line.replace('\n', '') for line in lines[:-1]]
    operators = lines[-1].replace('\n', '')

ans = 0
cur_box = []

for col in reversed(range(len(operators))):
    cur_num = ''

    for row in range(len(grid)):
        if grid[row][col].isdigit():
            cur_num += grid[row][col]

    if cur_num.isdigit():
        cur_box.append(int(cur_num))

    if operators[col] == '+':
        ans += sum(cur_box)
        cur_box = []

    if operators[col] == '*':
        ans += math.prod(cur_box)
        cur_box = []

print(ans)
