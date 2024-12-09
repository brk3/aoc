p = []
with open('input', 'r') as f:
    for line in f.readlines():
        row = []
        for char in line.strip():
            row.append(char)
        p.append(row)

def check_forward(row, col):
    i = col
    s = ''
    while i < len(p[row]) and s != 'XMAS':
        s += p[row][i]
        i += 1
    return 1 if s == 'XMAS' else 0

def check_back(row, col):
    i = col
    s = ''
    while i >= 0 and s != 'XMAS':
        s += p[row][i]
        i -= 1
    return 1 if s == 'XMAS' else 0

def check_up(row, col):
    i = row
    s = ''
    while i >= 0 and s != 'XMAS':
        s += p[i][col]
        i -= 1
    return 1 if s == 'XMAS' else 0

def check_down(row, col):
    i = row
    s = ''
    while i < len(p) and s != 'XMAS':
        s += p[i][col]
        i += 1
    return 1 if s == 'XMAS' else 0

def check_diags(row, col):
    count = 0
    # top left
    i = row
    j = col
    s = ''
    while i >= 0 and j >= 0 and s != 'XMAS':
        s += p[i][j]
        i -= 1
        j -= 1
    if s == 'XMAS': count += 1

    # top right
    i = row
    j = col
    s = ''
    while i >= 0 and j < len(p[row]) and s != 'XMAS':
        s += p[i][j]
        i -= 1
        j += 1
    if s == 'XMAS': count += 1

    # bottom left
    i = row
    j = col
    s = ''
    while i < len(p) and j >= 0 and s != 'XMAS':
        s += p[i][j]
        i += 1
        j -= 1
    if s == 'XMAS': count += 1

    # bottom right
    i = row
    j = col
    s = ''
    while i < len(p) and j < len(p[row]) and s != 'XMAS':
        s += p[i][j]
        i += 1
        j += 1
    if s == 'XMAS': count += 1

    return count

ans = 0
for row in range(len(p)):
    for col in range(len(p[row])):
        if p[row][col] == 'X':
            ans += check_forward(row, col)
            ans += check_back(row, col)
            ans += check_up(row, col)
            ans += check_down(row, col)
            ans += check_diags(row, col)

print(ans)
