from sys import stdin

from helpers import *




print_for_debug = PrintForDebug(False)




def solve():

    pass




t = int(stdin.readline())

for case_id in range(1, t + 1):

    f, l = (int(word) for word in stdin.readline().split())

    result = solve()

    print('Case #{}: {}'.format(case_id, result))
