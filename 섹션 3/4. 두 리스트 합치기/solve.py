import sys
import os


if os.name == 'nt':
    sys.path.insert(0, "\\".join(os.getcwd().split("\\")[:-2]))
else:
    sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge


@judge()
def solve():
    n = int(input())
    li1 = list(map(int, input().split()))
    m = int(input())
    li2 = list(map(int, input().split()))

    # return ' '.join(map(str, sorted(li1 + li2)))
    p1 = p2 = 0
    arr = []
    while p1 < n and p2 < m:
        if li1[p1] < li2[p2]:
            arr.append(li1[p1])
            p1 += 1
        else:
            arr.append(li2[p2])
            p2 += 1
    if p1 < n:
        arr += li1[p1:]
    elif p2 < m:
        arr += li2[p2:]

    return ' '.join(map(str, arr))


solve()
