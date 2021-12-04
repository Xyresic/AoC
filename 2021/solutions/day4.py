win_states = []
for i in range(5):
    win_states.append(set(j for j in range(5*i, 5*i+5)))
    win_states.append(set(j for j in range(i, 25, 5)))

def isWin(marks):
    for state in win_states:
        if len(state & marks) == 5:
            return True
    return False

with open('../inputs/input4.txt', 'r') as f:
    data = [s.strip() for s in f.readlines()]

    nums = [int(s) for s in data[0].split(',')]
    boards = []
    board = []
    for line in data[1:]:
        if len(line) != 0:
            board.extend([int(s) for s in line.split(' ') if s != ''])
        else:
            if board:
                boards.append(board)
            board = []
    marked = [set() for i in range(len(boards))]
    won = [False] * len(boards)
    won_count = 0
    for num in nums:
        for i, board in enumerate(boards):
            if num in board:
                marked[i].add(board.index(num))
        for i in range(len(boards)):
            marks = marked[i]
            if not won[i] and isWin(marks):
                # part 1 and 2
                if won_count == 0 or won_count == len(boards) - 1:
                    print(num * sum(n for j, n in enumerate(boards[i]) if j not in marks))
                won_count += 1
                won[i] = True
