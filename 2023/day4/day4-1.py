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

cards = []
with open('input', 'r') as f:
    for line in f:
        tokens = line.split(":")[1]
        num_lists = tokens.split("|")

        winning_nums = parse_nums(num_lists[0])
        our_nums = parse_nums(num_lists[1])

        winners = set(winning_nums).intersection(set(our_nums))
        card_value = 1 if winners else 0
        for i in range(len(winners)-1):
            card_value *= 2
        cards.append(card_value)

print(sum(cards))
