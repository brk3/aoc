# only 12 red cubes, 13 green cubes, and 14 blue cubes

sum = 0
with open('input', 'r') as f:
    lines = f.readlines()
    for line in lines:
        tokens = line.split(':')
        gameID = tokens[0]
        rounds = tokens[1].split(';')
        minRedNeeded = 0
        minBlueNeeded = 0
        minGreenNeeded = 0
        for _round in rounds:
            for cubeset in _round.split(','):
                cubetokens = cubeset.strip().split()
                color = cubetokens[1]
                numcubes = int(cubetokens[0])
                if (color == 'red' and numcubes > minRedNeeded):
                    minRedNeeded = numcubes
                elif (color == 'green' and numcubes > minGreenNeeded):
                    minGreenNeeded = numcubes
                elif (color == 'blue' and numcubes > minBlueNeeded):
                    minBlueNeeded = numcubes
        sum += minRedNeeded * minBlueNeeded * minGreenNeeded

print(sum)
