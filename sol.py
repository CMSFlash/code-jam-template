# Helpers


from sys import stderr


class PrintForDebug:

    def __init__(self, debug, file=stderr):
        self.debug = debug
        self.file = file

    def __call__(self, *args, **kwargs):
        if self.debug:
            print(*args, **kwargs, file=self.file)


# Solution


from sys import stdin


print_for_debug = PrintForDebug(False)


def solve():
    pass


def main():
    t = int(stdin.readline())
    for case_id in range(1, t + 1):
        x, y = (int(word) for word in stdin.readline().split())

        result = solve()

        print('Case #{}: {}'.format(case_id, result))


if __name__ == '__main__':
    main()
