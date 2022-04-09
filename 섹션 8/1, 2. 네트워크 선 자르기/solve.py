import sys
import os

sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge


def DFS(L):
    global n, dy
    if dy[L]:
        return dy[L]
    if L == 1 or L == 2:
        return L
    else:
        dy[L] = DFS(L - 1) + DFS(L - 2)
        return dy[L]


@judge()
def solve():
    global n, dy
    n = int(input())
    re = 0

    dy = [0] * (n + 1)

    ## Bottom up

    # dy[1] = 1
    # dy[2] = 2
    # for i in range(3, n + 1):
    #     dy[i] = dy[i - 1] + dy[i - 2]
    # re = dy[-1]

    # Top down (메모리제이션)
    re = DFS(n)
    return re


solve()
