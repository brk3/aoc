
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

        dial %= 100

        if dial == 0:
            count += 1

        print(f'{dial}')

print(f'ans: {count}')
