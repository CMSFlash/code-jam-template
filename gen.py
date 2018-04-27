import random




def legalize(n):

    return n




N = 100
X = 100
T = 1




print(T)

for case_id in range(T):

    n = random.randint(1, N)

    xs = []
    ys = []

    for i in range(n):

        x = legalize(random.randint(1, X))
        y = legalize(random.randint(1, X))

        xs.append(x)
        ys.append(y)

    print(n)

    for x, y in zip(xs, ys):

        print(x, y)
