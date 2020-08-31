from hashlib import md5

key = 'iwrupvqb'

# part one
suffix = 1
while True:
    if md5(f'{key}{suffix}'.encode()).hexdigest()[:5] == '00000':
        print(suffix)
        break
    suffix += 1

# part two
suffix = 1
while True:
    if md5(f'{key}{suffix}'.encode()).hexdigest()[:6] == '000000':
        print(suffix)
        break
    suffix += 1
