
intervals = []

with open('input') as f:
    for line in f:
        intervals.append(list(map(int, line.strip().split('-'))))

intervals.sort(key=lambda x: x[0])

merged = [intervals[0]]

for i in range(1, len(intervals)):
	if intervals[i][0] <= merged[-1][1]:
		merged[-1][1] = max(intervals[i][1], merged[-1][1])
	else:
		merged.append(intervals[i])

ans = 0
for start, stop in merged:
    ans += stop - start + 1

print(ans)
