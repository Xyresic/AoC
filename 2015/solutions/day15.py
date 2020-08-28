#less than 40 sugar
#less than 43 sprinkles+candy
#less than 67 chocolate

def make_cookie(part_two=False):
    scores = []
    for sugar in range(1, 40):
        for sprink in range(1, 42):
            for candy in range(1, 43 - sprink):
                choco = 100 - sugar - sprink - candy
                cap = sugar * 3 - sprink * 3 - candy
                dur = 3 * sprink
                flavor = 4 * candy - 2 * choco
                texture = 2 * choco - 3 * sugar
                if cap <= 0 or dur <= 0 or flavor <= 0 or texture <= 0\
                        or part_two and sugar * 2 + sprink * 9 + candy + choco * 8 != 500:
                    continue
                scores.append(cap * dur * flavor * texture)
    return max(scores)

#part one
print(make_cookie())

#part two
print(make_cookie(True))
