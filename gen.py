import random




def legalize(n):

    return n




L = int(1e6)
T = 1




print(T)

for case_id in range(T):

    l = legalize(random.randint(1, L))
    f = legalize(random.randint(1, l))
    print(f, l)
