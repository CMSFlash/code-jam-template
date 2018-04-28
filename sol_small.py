from sys import stdin

from helpers import *


print_for_debug = PrintForDebug(False)


def solve():
    pass


def main():
    t = int(stdin.readline())
    for case_id in range(1, t + 1):
        f, l = (int(word) for word in stdin.readline().split())

        result = solve()

        print('Case #{}: {}'.format(case_id, result))


if __name__ == '__main__':
    main()
