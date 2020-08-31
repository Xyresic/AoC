with open('../inputs/input2.txt', 'r') as f:
    data = [[int(val) for val in box.split('x')] for box in f.readlines()]

    # part one
    total = 0
    for box in data:
        products = [box[0] * box[1], box[0] * box[2], box[1] * box[2]]
        total += min(products)
        total += 2 * (sum(products))
    print(total)

    # part two
    ribbon = 0
    for box in data:
        ribbon += box[0] * box[1] * box[2]
        box.remove(max(box))
        ribbon += 2 * sum(box)
    print(ribbon)
