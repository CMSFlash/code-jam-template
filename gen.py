import random




def to_str(x):

    if x:
        result = 'x'
    else:
        result = 'o'

    return result




t = 1

print(t)

for caseId in range(t):

    r = random.randint(1, 20 + 1)
    c = random.randint(1, 20 + 1)
    print(r, c)

    for i in range(r):

        for j in range(c):

            print(to_str(random.choice([True, False])), end='')

        print()
