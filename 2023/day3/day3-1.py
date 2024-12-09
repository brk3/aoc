def is_symbol(s):
    return (not is_int(s)) and s != '.'

def is_int(i):
    try:
        int(i)
        return True
    except ValueError:
        return False

def is_part_num(schematic, x, y):
    if x > 0 and is_symbol(schematic[x-1][y]):
        print("value: {}, reason: top: {}".format(schematic[x][y], schematic[x-1][y]))
        return True
    if x > 0 and y < size-1 and is_symbol(schematic[x-1][y+1]):
        print("value: {}, reason: top right: {}".format(schematic[x][y], schematic[x-1][y+1]))
        return True
    if y < size-1 and is_symbol(schematic[x][y+1]):
        print("value: {}, reason: right: {}".format(schematic[x][y], schematic[x][y+1]))
        return True
    if x < size-1 and y < size-1 and is_symbol(schematic[x+1][y+1]):
        print("value: {}, reason: bottom right: {}".format(schematic[x][y], schematic[x+1][y+1]))
        return True
    if x < size-1 and is_symbol(schematic[x+1][y]):
        print("value: {}, reason: bottom: {}".format(schematic[x][y], schematic[x+1][y]))
        return True
    if x < size-1 and y > 0 and is_symbol(schematic[x+1][y-1]):
        print("value: {}, reason: bottom left: {}".format(schematic[x][y], schematic[x+1][y-1]))
        return True
    if y > 0 and is_symbol(schematic[x][y-1]):
        return True
        print("value: {}, reason: left: {}".format(schematic[x][y], schematic[x][y-1]))
    if x > 0 and y > 0 and is_symbol(schematic[x-1][y-1]):
        print("value: {}, reason: top left: {}".format(schematic[x][y], schematic[x-1][y-1]))
        return True
    return False

schematic = []
with open('input', 'r') as f:
    for line in f:
        schematic.append(list(line.strip()))
    size = len(schematic)

    valid_nums = []
    valid = False
    num_buffer = ''
    for x in range(size):
        for y in range(size):
            if is_int(schematic[x][y]):
                num_buffer += schematic[x][y]
                if is_part_num(schematic, x, y):
                    valid = True
                    # cover the bottom corner case
                    if x == size-1 and y == size-1:
                        valid_nums.append(int(num_buffer))
            elif num_buffer != '':
                print(num_buffer)
                if valid:
                    valid_nums.append(int(num_buffer))
                else:
                    print("XXX: invalid part num: {}".format(num_buffer))
                num_buffer = ''
                valid = False

    print(valid_nums)
    print(sum(valid_nums))

