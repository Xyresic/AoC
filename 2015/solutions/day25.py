row = 3010
col = 3019

# part one
current = 20151125
iters = sum(range(col + 1)) + sum(range(col, col + row -1))
for n in range(iters - 1):
    current = current * 252533 % 33554393
print(current)
