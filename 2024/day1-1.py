l = []
r = []
with open('input') as file:
    for line in file:
        tokens = line.split()
        l.append(int(tokens[0]))
        r.append(int(tokens[1]))

l.sort()
r.sort()

distance = 0
for i in range(len(l)):
    distance += abs(l[i] - r[i])

print(distance)
