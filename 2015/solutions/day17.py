from itertools import combinations

data = [43, 3, 4, 10, 21, 44, 4, 6, 47, 41, 34, 17, 17, 44, 36, 31, 46, 9, 27, 38]

# part one
count = 0
for i in range(4, 21):
    for com in combinations(data, i):
        if sum(com) == 150:
            count += 1
print(count)

# part two
count = 0
for com in combinations(data, 4):
    if sum(com) == 150:
        count += 1
print(count)
