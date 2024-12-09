p = []
with open('input', 'r') as f:
    for line in f.readlines():
        row = []
        for char in line.strip():
            row.append(char)
        p.append(row)

def check_diags(row, col):
    if ((row < 1 or row == len(p)-1) or
            (col < 1 or col == len(p[row])-1)):
        return 0

    # top left and bottom right
    x1 = ((p[row-1][col-1] == 'M' and p[row+1][col+1] == 'S') or
            (p[row-1][col-1] == 'S' and p[row+1][col+1] == 'M'))

    # top right and bottom left
    x2 = ((p[row-1][col+1] == 'M' and p[row+1][col-1] == 'S') or
            (p[row-1][col+1] == 'S' and p[row+1][col-1] == 'M'))

    return 1 if x1 and x2 else 0

ans = 0
for row in range(len(p)):
    for col in range(len(p[row])):
        if p[row][col] == 'A':
            ans += check_diags(row, col)

print(ans)
