
fresh = []
available = []

with open('input') as f:
    in_ranges = True
    for line in f:
        if len(line.strip()) == 0:
            in_ranges = False
            continue
        if in_ranges:
            fresh.append(line.strip())
        else:
            available.append(line.strip())

count = 0

for a in available:
    for f in fresh:
        start, stop = f.split('-')
        if int(a) in range(int(start), int(stop)+1):
            count += 1
            break

print(count)
