from itertools import combinations
from functools import reduce

i = set([int(num.strip()) for num in open('../inputs/input24.txt').readlines()])

#part one
smallest_fronts = set()
min_front = -1
for n in range(5, 20):
    for front in combinations(i, n):
        if sum(front) != 512:
            continue
        remainder = i - set(front)
        valid = False
        for j in range(5, 25 - n):
            for mid in combinations(remainder, j):
                if sum(mid) != 512:
                    continue
                if min_front == -1 or n == min_front:
                    min_front = n
                    valid = True
                    break
            if n == min_front and valid:
                break
        if valid:
            smallest_fronts.add(front)
        if min_front != -1 and n > min_front:
            break
    if min_front != -1:
        break
smallest_fronts = [reduce(lambda x, y: x * y, front) for front in smallest_fronts]
print(min(smallest_fronts))

#part two
smallest_fronts = set()
min_front = -1
for n in range(4, 18):
    for front in combinations(i, n):
        if sum(front) != 384:
            continue
        remainder = i - set(front)
        for j in range(4, 22 - n):
            for mid in combinations(remainder, j):
                if sum(mid) != 384:
                    continue
                leftover = remainder - set(mid)
                valid = False
                for k in range(4, 26 - n - j):
                    for penult in combinations(leftover, k):
                        if sum(penult) != 384:
                            continue
                        if min_front == -1 or n == min_front:
                            min_front = n
                            valid = True
                            break
                    if n == min_front and valid:
                        break
                if valid:
                    smallest_fronts.add(front)
                    break
            if n == min_front:
                break
        if min_front != -1 and n > min_front:
            break
    if min_front != -1:
        break
smallest_fronts = [reduce(lambda x, y: x * y, front) for front in smallest_fronts]
print(min(smallest_fronts))