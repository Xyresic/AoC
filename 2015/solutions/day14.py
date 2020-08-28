i = open('../inputs/input14.txt').readlines()

dist = [0] * 9
points = [0] * 9
for n in range(2503):
    if n % 131 < 7:
        dist[0] += 19
    if n % 43 < 15:
        dist[1] += 3
    if n % 173 < 9:
        dist[2] += 19
    if n % 167 < 9:
        dist[3] += 19
    if n % 89 < 7:
        dist[4] += 13
    if n % 151 < 6:
        dist[5] += 25
    if n % 41 < 3:
        dist[6] += 14
    if n % 53 < 16:
        dist[7] += 3
    if n % 149 < 6:
        dist[8] += 25
    front = max(dist)
    for n in range(9):
        if dist[n] == front:
            points[n] += 1

#part one
print(max(dist))

#part two
print(max(points))