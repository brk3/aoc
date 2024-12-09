def rotate(start):
    directions = ['up', 'right', 'down', 'left']
    pos = [i for i in range(len(directions)) if directions[i] == start][0]
    return directions[(pos+1) % len(directions)]

def has_loop(p):
    direction = 'up'
    row, col = guard[0], guard[1]
    visited = set()
    while row >= 0 and row < len(p) and col >= 0 and col < len(p[0]):
        #print(row, col, direction)
        if (row, col, direction) in visited:
            return True
        else:
            visited.add((row, col, direction))

        if direction == 'up':
            if row > 0 and p[row-1][col] == '#':
                direction = rotate(direction)
            else:
                row -= 1

        elif direction == 'down':
            if row < len(p)-1 and p[row+1][col] == '#':
                direction = rotate(direction)
            else:
                row += 1

        elif direction == 'right':
            if col < len(p[0])-1 and p[row][col+1] == '#':
                direction = rotate(direction)
            else:
                col += 1

        elif direction == 'left':
            if col > 0 and p[row][col-1] == '#':
                direction = rotate(direction)
            else:
                col -= 1
    return False

p = []
guard = []
with open('input', 'r') as f:
    row = 0
    for line in f:
        cols = []
        col = 0
        for c in line.strip():
            if c == '^':
                guard = [row, col]
            cols.append(c)
            col += 1
        p.append(cols)
        row += 1

def print_maze(p):
    for row in p:
        print(''.join(row))

ans = 0
for row in range(len(p)):
    for col in range(len(p[0])):
        #if p[row][col] == '#': continue # faster?
        temp = p[row][col]
        p[row][col] = '#'
        if has_loop(p):
            print(row, col, ans)
            ans += 1
        p[row][col] = temp

print(ans)
