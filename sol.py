# Helpers


from sys import stderr


class DebugPrinter:
    def __init__(self, debug, file=stderr):
        self.debug = debug
        self.file = file

    def __call__(self, *args, **kwargs):
        if self.debug:
            print(*args, **kwargs, file=self.file)


# Algorithms


import heapq
import queue
import decimal


def round_half_up(x):
    x = decimal.Decimal(x)
    n = x.to_integral(rounding=decimal.ROUND_HALF_UP)
    return n


class PriorityQueue(queue.PriorityQueue):
    def __init__(self, initial=[], heapified=False):
        super().__init__(maxsize=0)
        if not heapified:
            heapq.heapify(initial)
        self.queue = initial

    def __str__(self):
        return str(self.queue)


# Solution


from sys import stdin


print_for_debug = DebugPrinter(False)


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
