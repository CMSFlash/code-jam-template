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

        print(n)
        for l, f in zip(ls, fs):
            print(l, f)


if __name__ == '__main__':
    main()
