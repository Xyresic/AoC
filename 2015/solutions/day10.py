from itertools import groupby

def look_say(num):
    start = '1113122113'
    for i in range(num):
        start = ''.join([f'{len(list(group))}{key}' for key, group in groupby(start)])
    return len(start)

# part one
print(look_say(40))

# part two
print(look_say(50))
