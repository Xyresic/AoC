dist = [0] * 9
points = [0] * 9
for i in range(2503):
    if i % 131 < 7:
        dist[0] += 19
    if i % 43 < 15:
        dist[1] += 3
    if i % 173 < 9:
        dist[2] += 19
    if i % 167 < 9:
        dist[3] += 19
    if i % 89 < 7:
        dist[4] += 13
    if i % 151 < 6:
        dist[5] += 25
    if i % 41 < 3:
        dist[6] += 14
    if i % 53 < 16:
        dist[7] += 3
    if i % 149 < 6:
        dist[8] += 25
    front = max(dist)
    for j in range(9):
        if dist[j] == front:
            points[j] += 1

# part one
print(max(dist))

# part two
print(max(points))
