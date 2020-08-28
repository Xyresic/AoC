import itertools as it

i = '1113122113'

def look_say(num):
    global i
    for n in range(num):
        i = ''.join([f'{len(list(group))}{key}' for key, group in it.groupby(i)])
    return len(i)

#part one
print(look_say(40))

#part two
print(look_say(10))
