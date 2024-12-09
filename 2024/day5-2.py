rules=[]
pages=[]
with open('input', 'r') as f:
    for line in f:
        if '|' in line:
            tokens = line.strip().split('|')
            rules.append((int(tokens[0]), int(tokens[1])))
        if ',' in line:
            pages.append([int(n) for n in line.strip().split(',')])

rules_map = {}
for rule in rules:
    if rule[0] not in rules_map: rules_map[rule[0]] = []
    rules_map[rule[0]].append(rule[1])

ans = 0
for page in pages:
    found = False
    for i in range(len(page)):
        cur_rules = rules_map.get(page[i], [])
        for j in range(i):
            if page[j] in cur_rules:
                page[i], page[j] = page[j], page[i]
                found = True
    if found:
        ans += page[len(page)//2]

print(ans)
