
ans = 0

with open('input', 'r') as f:
    for line in f:
        nums = [int(i) for i in line.strip()]

        pos = -1
        cur = ''

        for i in reversed(range(12)):
            val = float('-inf')
            for j in range(pos+1, len(nums)-i):
                if nums[j] > val:
                    val = nums[j]
                    pos = j
            cur += str(val)

        ans += int(cur)

print(ans)
