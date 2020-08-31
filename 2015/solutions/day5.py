with open('../inputs/input5.txt', 'r') as f:
    data = f.readlines()

    # part one
    def tri_vowel(string):
        return string.count('a') + string.count('e') + string.count('i') + string.count('o') + string.count('u') > 2

    def has_double(string):
        for i in range(len(string) - 1):
            if string[i] == string[i + 1]:
                return True
        return False

    niceStrings = [s for s in data if 'ab' not in s
                   and 'cd' not in s
                   and 'pq' not in s
                   and 'xy' not in s
                   and tri_vowel(s) and has_double(s)]
    print(len(niceStrings))

    # part two
    def double_pair(string):
        for i in range(len(string) - 3):
            if string[i:i + 2] in string[i + 2:]:
                return True
        return False

    def letter_sandwich(string):
        for i in range(len(string) - 2):
            if string[i + 2] == string[i]:
                return True
        return False

    niceStrings = [s for s in data if double_pair(s) and letter_sandwich(s)]
    print(len(niceStrings))
