import hashlib

i = 'iwrupvqb'

#part one
suffix = 1
while True:
    if hashlib.md5(f'{i}{suffix}'.encode()).hexdigest()[:5] == '00000':
        print(suffix)
        break
    suffix += 1

#part two
suffix = 1
while True:
    if hashlib.md5(f'{i}{suffix}'.encode()).hexdigest()[:6] == '000000':
        print(suffix)
        break
    suffix += 1