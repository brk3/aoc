from collections import Counter

l = []
r = []
with open('input') as file:
    for line in file:
        tokens = line.split()
        l.append(int(tokens[0]))
        r.append(int(tokens[1]))

count = Counter(r)
similarity = 0
for num in l:
    similarity += num * count[num]

print(similarity)
