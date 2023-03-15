import os
import sys
if os.name == 'nt':
    sys.path.insert(0, "\\".join(os.getcwd().split("\\")[:-2]))
else:
    sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))


from judge import judge


@judge(start=1, end=2)
def solve():
    cards = [i for i in range(1, 21)]
    for i in range(10):
        s, e = map(lambda x: x - 1, map(int, input().split()))
        for j in range((e - s + 1) // 2):
            cards[s + j], cards[e-j] = cards[e - j], cards[s + j]
    return ' '.join(map(str, cards))


solve()
