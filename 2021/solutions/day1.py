with open('../inputs/input1.txt', 'r') as f:
    data = [int(s.strip()) for s in f.readlines()]

    # part 1
    count1 = 0
    count2 = 0
    for i in range(len(data) - 1):
        if data[i+1] > data[i]:
            count1 += 1
        if i < len(data) - 2 and sum(data[i+1:i+4]) > sum(data[i:i+3]):
            count2 += 1
    print(count1)
    print(count2)
