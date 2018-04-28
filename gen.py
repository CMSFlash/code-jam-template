import random


T = 1
N = 1000
X = int(1e6)


def legalize(x):
    return x


def main():
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


if __name__ == '__main__':
    main()
