def is_int(i):
    try:
        int(i)
        return True
    except ValueError:
        return False

# check forward and back to build number
def parse_int(schematic, x, y):
    if not is_int(schematic[x][y]):
        raise ValueError('parse_int() expects a digit')
    numstring = schematic[x][y]
    i = y-1
    while i >= 0 and is_int(schematic[x][i]):
        numstring = schematic[x][i] + numstring
        i -= 1
    i = y+1
    while i < len(schematic) and is_int(schematic[x][i]):
        numstring = numstring + schematic[x][i]
        i += 1
    return numstring

def get_gears(schematic, x, y):
    gears = []

    if x > 0 and is_int(schematic[x-1][y]):
        top = parse_int(schematic, x-1, y)
        gears.append(top)
    else:
        # only check corners if top isn't valid
        if x > 0 and y < size-1 and is_int(schematic[x-1][y+1]):
            top_right = parse_int(schematic, x-1, y+1)
            gears.append(top_right)
        if x > 0 and y > 0 and is_int(schematic[x-1][y-1]):
            top_left = parse_int(schematic, x-1, y-1)
            gears.append(top_left)

    if y < size-1 and is_int(schematic[x][y+1]):
        right = parse_int(schematic, x, y+1)
        gears.append(right)
    if y > 0 and is_int(schematic[x][y-1]):
        left = parse_int(schematic, x, y-1)
        gears.append(left)

    if x < size-1 and is_int(schematic[x+1][y]):
        bottom = parse_int(schematic, x+1, y)
        gears.append(bottom)
    else:
        if x < size-1 and y < size-1 and is_int(schematic[x+1][y+1]):
            bottom_right = parse_int(schematic, x+1, y+1)
            gears.append(bottom_right)
        if x < size-1 and y > 0 and is_int(schematic[x+1][y-1]):
            bottom_left = parse_int(schematic, x+1, y-1)
            gears.append(bottom_left)

    return gears

schematic = []
with open('input', 'r') as f:
    for line in f:
        schematic.append(list(line.strip()))

# we assume schematic is a square (rows and cols same length)
size = len(schematic)
ratio = 0
for x in range(size):
    for y in range(size):
        if schematic[x][y] == '*':
            gears = get_gears(schematic, x, y)
            if len(gears) == 2:
                print(gears)
                ratio += int(gears[0]) * int(gears[1])
print(ratio)
