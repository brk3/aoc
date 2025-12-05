
ans = 0

with open('input', 'r') as f:
    for line in f:
        a_val = 0
        a_pos = 0

        nums = [int(i) for i in line.strip()]

        for i in range(len(nums)-1):
            if nums[i] > a_val:
                a_val = nums[i]
                a_pos = i

        b_val = max(nums[a_pos+1:])

        #print(f'{a_val}{b_val}')
        ans += int(f'{a_val}{b_val}')

print(ans)
