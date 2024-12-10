def disk_to_blocks(disk):
    blocks = []
    block_id = 0
    for i in range(len(disk)):
        if i % 2 == 0:
            for j in range(int(disk[i])):
                blocks.append(block_id)
            block_id += 1
        else:
            for j in range(int(disk[i])):
                blocks.append(".")
    return blocks

with open('input', 'r') as f:
    disk = f.read().strip()

blocks = disk_to_blocks(disk)
i = 0
j = len(blocks)-1

while i < j:
    if blocks[i] != '.': i += 1
    if blocks[j] == '.': j -= 1
    if blocks[i] == '.' and blocks[j] != '.':
        blocks[i], blocks[j] = blocks[j], blocks[i]

ans = 0
for i, j in enumerate(blocks):
    if j == '.': break
    ans += int(i) * int(j)

print(ans)
