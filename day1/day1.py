nums = []
with open('input', 'r') as f:
    for i in f.readlines():
        num_str = ''
        for c in i:
            try:
                num_str += str(int(c))
                break
            except ValueError:
                pass
        for c in i[::-1]:
            try:
                num_str += str(int(c))
                break
            except ValueError:
                pass
        nums.append(int(num_str))

print(sum(nums))
