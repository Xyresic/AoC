i = open('../inputs/input5.txt', 'r').readlines()


# part one
def triVowel(string):
    return string.count('a') + string.count('e') + string.count('i') + string.count('o') + string.count('u') > 2

def hasDouble(string):
    for n in range(len(string) - 1):
        if string[n] == string[n + 1]:
            return True
    return False

niceStrings = [s for s in i if 'ab' not in s
               and 'cd' not in s
               and 'pq' not in s
               and 'xy' not in s
               and triVowel(s) and hasDouble(s)]
print(len(niceStrings))

# part two
def doublePair(string):
    for n in range(len(string) - 3):
        if string[n:n+2] in string[n+2:]:
            return True
    return False

def letterSandwich(string):
    for n in range(len(string) - 2):
        if string[n+2] == string[n]:
            return True
    return False

niceStrings = [s for s in i if doublePair(s) and letterSandwich(s)]
print(len(niceStrings))