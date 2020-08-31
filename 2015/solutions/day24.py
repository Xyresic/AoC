from itertools import combinations
from functools import reduce

weights = set([int(num.strip()) for num in open('../inputs/input24.txt').readlines()])

# part one
smallestFronts = set()
minFront = -1
for i in range(5, 20):
    for front in combinations(weights, i):
        if sum(front) != 512:
            continue
        remainder = weights - set(front)
        valid = False
        for j in range(5, 25 - i):
            for mid in combinations(remainder, j):
                if sum(mid) != 512:
                    continue
                if minFront == -1 or i == minFront:
                    minFront = i
                    valid = True
                    break
            if i == minFront and valid:
                break
        if valid:
            smallestFronts.add(front)
        if minFront != -1 and i > minFront:
            break
    if minFront != -1:
        break
smallestFronts = [reduce(lambda x, y: x * y, front) for front in smallestFronts]
print(min(smallestFronts))

# part two
smallestFronts = set()
minFront = -1
for i in range(4, 18):
    for front in combinations(weights, i):
        if sum(front) != 384:
            continue
        remainder = weights - set(front)
        for j in range(4, 22 - i):
            for mid in combinations(remainder, j):
                if sum(mid) != 384:
                    continue
                leftover = remainder - set(mid)
                valid = False
                for k in range(4, 26 - i - j):
                    for penult in combinations(leftover, k):
                        if sum(penult) != 384:
                            continue
                        if minFront == -1 or i == minFront:
                            minFront = i
                            valid = True
                            break
                    if i == minFront and valid:
                        break
                if valid:
                    smallestFronts.add(front)
                    break
            if i == minFront:
                break
        if minFront != -1 and i > minFront:
            break
    if minFront != -1:
        break
smallestFronts = [reduce(lambda x, y: x * y, front) for front in smallestFronts]
print(min(smallestFronts))
