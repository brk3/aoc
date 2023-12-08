def extract(s):
    words = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    tokens = []
    for i in range(len(s)):
        try:
            tokens.append(str(int(s[i])))
            continue
        except ValueError:
            pass
        for k, v in words.items():
            if s[i:i+len(k)] == k:
                tokens.append(v)
    return tokens

nums = []
with open('input', 'r') as f:
    for i in f.readlines():
        tokens = extract(i)
        nums.append(int("{0}{1}".format(tokens[0], tokens[-1])))
print(sum(nums))
