
with open('input', 'r') as f:
    ids = f.read().strip().split(',')

ans = 0

for n in ids:
    start, end = n.split('-')
    for i in range(int(start), int(end)+1):
        s = str(i)
        mid = len(s) // 2
        if s[:mid] == s[mid:]:
            ans += i

print(ans)
