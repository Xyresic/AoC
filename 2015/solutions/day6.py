i = open('../inputs/input6.txt', 'r').readlines()

#part one
lights = [False] * 1000000
for line in i:
    instructions = line.split()
    if 'toggle' in line:
        botLeft = [int(c) for c in instructions[1].split(',')]
        topRight = [int(c) for c in instructions[3].split(',')]
        for y in range(topRight[1] - botLeft[1] + 1):
            for x in range(topRight[0] - botLeft[0] + 1):
                index = (botLeft[1] + y) * 1000 + botLeft[0] + x
                lights[index] = not lights[index]
    else:
        botLeft = [int(c) for c in instructions[2].split(',')]
        topRight = [int(c) for c in instructions[4].split(',')]
        if 'off' in line:
            for y in range(topRight[1] - botLeft[1] + 1):
                for x in range(topRight[0] - botLeft[0] + 1):
                    lights[(botLeft[1] + y) * 1000 + botLeft[0] + x] = False
        else:
            for y in range(topRight[1] - botLeft[1] + 1):
                for x in range(topRight[0] - botLeft[0] + 1):
                    lights[(botLeft[1] + y) * 1000 + botLeft[0] + x] = True
print(lights.count(True))

#part two
lights = [0] * 1000000
for line in i:
    instructions = line.split()
    if 'toggle' in line:
        botLeft = [int(c) for c in instructions[1].split(',')]
        topRight = [int(c) for c in instructions[3].split(',')]
        for y in range(topRight[1] - botLeft[1] + 1):
            for x in range(topRight[0] - botLeft[0] + 1):
                lights[(botLeft[1] + y) * 1000 + botLeft[0] + x] += 2
    else:
        botLeft = [int(c) for c in instructions[2].split(',')]
        topRight = [int(c) for c in instructions[4].split(',')]
        if 'off' in line:
            for y in range(topRight[1] - botLeft[1] + 1):
                for x in range(topRight[0] - botLeft[0] + 1):
                    index = (botLeft[1] + y) * 1000 + botLeft[0] + x
                    lights[index] = lights[index] - 1 if lights[index] - 1 > 0 else 0
        else:
            for y in range(topRight[1] - botLeft[1] + 1):
                for x in range(topRight[0] - botLeft[0] + 1):
                    lights[(botLeft[1] + y) * 1000 + botLeft[0] + x] += 1
print(sum(lights))