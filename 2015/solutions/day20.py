minPresents = 33100000

# part one
maxSearch = minPresents // 10
presents = [0] * maxSearch
for i in range(1, maxSearch + 1):
    for j in range(i, maxSearch, i):
        presents[j] += i * 10
for i in range(maxSearch):
    if presents[i] >= minPresents:
        print(i)
        break

# part two
maxSearch = minPresents // 11
presents = [0] * maxSearch
for i in range(1, maxSearch + 1):
    for j in range(i, min(maxSearch, i * 50 + 1), i):
        presents[j] += i * 11
for i in range(maxSearch):
    if presents[i] >= minPresents:
        print(i)
        break
