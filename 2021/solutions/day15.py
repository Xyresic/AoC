import heapq
from collections import defaultdict

def astar(data):
    goal = (len(data) - 1, len(data[0]) - 1)

    class Node:
        def __init__(self, coord, g):
            self.coord = coord
            self.x = coord[1]
            self.y = coord[0]
            self.g = g
            self.f = g + goal[0] + goal[1] - self.y - self.x

        def __hash__(self):
            return hash(self.coord)

        def __eq__(self, other):
            return self.coord == other.coord

        def __lt__(self, other):
            return self.f < other.f

    start = Node((0, 0), 0)
    to_expand = [start]
    g = defaultdict(lambda: float('inf'))
    g[start] = 0

    while to_expand:
        if to_expand[0].coord == goal:
            return to_expand[0].g
        cur = heapq.heappop(to_expand)
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                x = cur.x + dx
                y = cur.y + dy
                if (abs(dy) ^ abs(dx)) and 0 <= x < len(data[0]) and 0 <= y < len(data):
                    neighbor = Node((y, x), cur.g + data[y][x])
                    if neighbor.g < g[neighbor]:
                        g[neighbor] = neighbor.g
                        heapq.heappush(to_expand, neighbor)

with open('../inputs/input15.txt', 'r') as f:
    data = [[int(c) for c in s.strip()] for s in f.readlines()]

    # part 1
    print(astar(data))

    # part 2
    dim_y = len(data)
    dim_x = len(data[0])
    full = [[0 for __ in range(dim_x * 5)] for _ in range(dim_y * 5)]
    for dy in range(5):
        for dx in range(5):
            for y in range(dim_y):
                for x in range(dim_x):
                    full[y + dy * dim_y][x + dx * dim_x] = (data[y][x] + dx + dy - 1) % 9 + 1
    print(astar(full))
