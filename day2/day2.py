# only 12 red cubes, 13 green cubes, and 14 blue cubes

sum = 0
with open('input', 'r') as f:
    lines = f.readlines()
    for line in lines:
        tokens = line.split(':')
        gameID = tokens[0]
        rounds = tokens[1].split(';')
        validgame = True
        for _round in rounds:
            for cubeset in _round.split(','):
                cubetokens = cubeset.strip().split()
                color = cubetokens[1]
                numcubes = int(cubetokens[0])
                if (color == 'red' and numcubes > 12 or
                        color == 'green' and numcubes > 13 or
                        color == 'blue' and numcubes > 14):
                    validgame = False
        if validgame:
            sum += int(gameID.split()[1])

print(sum)
