#puzzles = ['xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))']
# 2,4
# 5,5
# 11,8
# 8,5

with open('input', 'r') as f:
    puzzles = f.readlines()

pairs = []
for puzzle in puzzles:
    i = 0
    while i < len(puzzle):
        x = puzzle.find('mul(', i)
        if x > -1:
            y = x + len('mul(')
            s = ''
            while y < len(puzzle):
                if puzzle[y].isdigit() or puzzle[y] == ',':
                    s += puzzle[y]
                    y += 1
                elif puzzle[y] == ')':
                    i = y
                    pairs.append(s)
                    break
                else:
                    break
        i += 1

ans = 0
for pair in pairs:
    tokens = pair.split(',')
    if len(tokens) == 2:
        ans += int(tokens[0]) * int(tokens[1])

assert(ans == 155955228)
