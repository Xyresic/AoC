def get_cost(data, target, part_one=True):
    cost = 0
    for num in data:
        dist = abs(target - num)
        cost += dist * (1 if part_one else (dist + 1) / 2)
    return cost

with open('../inputs/input7.txt', 'r') as f:
    data = sorted([int(s) for s in f.read().split(',')])
    target = data[len(data) // 2]

    # part 1
    print(get_cost(data, target))

    # part 2
    print(int(min(get_cost(data, target + i, part_one=False) for i in range(-150, 150))))
