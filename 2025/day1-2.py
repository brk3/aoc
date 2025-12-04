
dial = 50
count = 0

with open('input', 'r') as f:
    for line in f:
        direction = line[0]
        val = int(line[1:])

        for i in range(1, val+1):
            if direction == 'L':
                dial -= 1
            else:
                dial += 1
            dial %= 100
            if dial == 0:
                count += 1

print(f'ans: {count}')
