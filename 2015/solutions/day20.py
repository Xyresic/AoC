i = 33100000

#part one
presents = [0] * (i // 10)
for n in range(1, i // 10 + 1):
    for m in range(n, i // 10, n):
        presents[m] += n * 10
for n in range(i // 10):
    if presents[n] >= i:
        print(n)
        break

#part two
presents = [0] * (i // 11)
for n in range(1, i // 11 + 1):
    for m in range(n, min(i // 11, n * 50 + 1), n):
        presents[m] += n * 11
for n in range(i // 11):
    if presents[n] >= i:
        print(n)
        break