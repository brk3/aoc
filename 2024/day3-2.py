#puzzles = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]

with open('input', 'r') as f:
    puzzles = f.readlines()

pairs = []
for puzzle in puzzles:
    i = 0
    while i < len(puzzle):
        mul = puzzle.find('mul(', i)
        do = puzzle.find('do()', i)
        dont = puzzle.find('don\'t()', i)

        check = [x for x in [mul, do, dont] if x > -1]
        if len(check) < 1:
            break
        first = min(check)

        if first == do:
            pairs.append('do()')
            i = do + len('do()')-1
        elif first == dont:
            pairs.append('don\'t()')
            i = dont + len('don\'t()')-1
        elif mul > -1:
            y = mul + len('mul(')
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
skip = False
for pair in pairs:
    if pair == 'do()':
        skip = False
        continue
    if pair == 'don\'t()':
        skip = True
        continue
    if skip is False:
        tokens = pair.split(',')
        if len(tokens) == 2:
            ans += int(tokens[0]) * int(tokens[1])

print(ans)
