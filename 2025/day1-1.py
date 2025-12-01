
dial = 50
count = 0

with open('input', 'r') as f:
    for line in f:
        direction = line[0]
        val = int(line[1:])

        if direction == 'L':
            dial -= val
        else:
            dial += val

        while dial < 0:
            dial = 99 - abs(dial) + 1

        while dial > 99:
            dial = dial - 99 - 1

        if dial == 0:
            count += 1

        print(f'{dial}')

print(f'ans: {count}')
