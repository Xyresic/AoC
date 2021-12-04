with open('../inputs/input1.txt', 'r') as f:
    data = [int(s.strip()) for s in f.readlines()]

    count1 = 0
    count2 = 0
    window = sum(data[0:3])
    for i in range(len(data) - 1):
        if data[i + 1] > data[i]:
            count1 += 1
        if i < len(data) - 3 and window < (window := window - data[i] + data[i + 3]):
            count2 += 1

    # part 1
    print(count1)

    # part 2
    print(count2)
