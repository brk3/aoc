def is_int(i):
    try:
        int(i)
        return True
    except ValueError:
        return False

def parse_nums(l):
    return [int(i) for i in l]

# naive approach, too slow for large inputs
# def build_range_map(ranges):
    # m = {}
    # for r in ranges:
        # dest_start = r[0]
        # source_start = r[1]
        # range_length = r[2]
        # for i, j in enumerate(range(source_start, source_start+range_length)):
            # m[j] = dest_start + i
    # return m

def source_to_dest(m, seed):
    for r in m:
        dest = r[0]
        source = r[1]
        length = r[2]
        if seed >= source and seed <= source + length:
            return dest + (seed - source)
    return seed

def main():
    with open('input', 'r') as f:
        lines = f.readlines()

    seeds = parse_nums(lines[0].split(':')[1].split())
    ranges = []
    maps = []
    for i in range(3, len(lines)):
        line = lines[i]
        if line == '\n':
            continue
        if is_int(line[0]):
            ranges.append(parse_nums(line.split()))
            if i == len(lines)-1:
                maps.append(ranges)
        else:
            maps.append(ranges)
            ranges = []

    locations = []
    for seed in seeds:
        for m in maps:
            seed = source_to_dest(m, seed)
        locations.append(seed)

    print(locations)
    print(min(locations))

if __name__ == '__main__':
    main()
