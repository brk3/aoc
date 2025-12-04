def repeatedSubstringPattern(s):
    for i in range(1, len(s)):
        ss = s[:i]
        if ss * (len(s) // i) == s:
            return True
    return False

with open('input', 'r') as f:
    ids = f.read().strip().split(',')

ans = 0

for n in ids:
    start, end = n.split('-')
    for i in range(int(start), int(end)+1):
        if repeatedSubstringPattern(str(i)):
            ans += i

print(ans)
