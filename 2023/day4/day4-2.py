def is_int(i):
    try:
        int(i)
        return True
    except ValueError:
        return False

def parse_nums(s):
    nums = []
    buf = ''
    for i in s:
        if is_int(i):
            buf += i
        else:
            if buf != '':
                nums.append(int(buf))
                buf = ''
    return nums

lines = []
with open('input', 'r') as f:
    lines = f.readlines()

card_counts = [1] * len(lines)
for i in range(len(lines)):
    line = lines[i]
    tokens = line.split(":")[1]
    num_lists = tokens.split("|")
    winning_nums = parse_nums(num_lists[0])
    our_nums = parse_nums(num_lists[1])
    winners = set(winning_nums).intersection(set(our_nums))

    #for _ in range(card_counts[i]):
    #    for j in range(i+1, i+len(winners)+1):
    #        card_counts[j] += 1

    # increase each count by 1 * number of current copies
    for j in range(i+1, i+len(winners)+1):
        card_counts[j] += card_counts[i]

    print(len(winners))

print(card_counts)
print(sum(card_counts))
