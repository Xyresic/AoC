from collections import deque

with open('../inputs/input10.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]

    syntax_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    auto_scores = {'(': 1, '[': 2, '{': 3, '<': 4}
    closers = {')', '}', ']', '>'}
    match = {')': '(', '}': '{', ']': '[', '>': '<'}
    syntax_score = 0
    line_scores = []
    for line in data:
        auto_score = 0
        d = deque()
        corrupted = False
        for c in line:
            if corrupted:
                break
            if c in closers:
                if d[-1] != match[c]:
                    syntax_score += syntax_scores[c]
                    corrupted = True
                    break
                else:
                    d.pop()
            else:
                d.append(c)
        if not corrupted:
            for c in reversed(d):
                auto_score *= 5
                auto_score += auto_scores[c]
            line_scores.append(auto_score)

    # part 1
    print(syntax_score)

    # part 2
    print(sorted(line_scores)[len(line_scores) // 2])
