import random


T = 1
N = 1000
L = int(1e6)


def legalize(n):
    return n


def main():
    print(T)
    for case_id in range(T):
        n = random.randint(1, N)
        ls = []
        fs = []

        for i in range(n):
            l = legalize(random.randint(1, L))
            f = legalize(random.randint(1, l))

<<<<<<< HEAD
        print(n)
        for l, f in zip(ls, fs):
            print(l, f)
=======
N = 100
X = 100
T = 1




print(T)
>>>>>>> 13d62588a61207ba3b9c96b13d2b4c594329dc62


<<<<<<< HEAD
if __name__ == '__main__':
    main()
=======
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
>>>>>>> 13d62588a61207ba3b9c96b13d2b4c594329dc62
