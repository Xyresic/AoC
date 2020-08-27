i = open('../inputs/input8.txt', 'r').readlines()

#part one
print(sum([len(line) - len(eval(line)) - 1 for line in i]))

#part two
print(sum([2 + line.count('\\') + line.count('"') for line in i]))