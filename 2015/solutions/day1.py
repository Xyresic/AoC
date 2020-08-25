i = open('../inputs/input1.txt', 'r').read()

#part one
print(i.count('(') - i.count(')'))

#part two
pos = 1
floor = 0
for c in i:
    if c == '(':
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        print(pos)
        break
    pos += 1