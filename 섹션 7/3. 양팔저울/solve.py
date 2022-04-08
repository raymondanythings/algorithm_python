import sys
import os

sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge


def DFS(L, total):
    global n, G, s, res
    if L == n:
        if 0 < total:
            res.add(total)
    else:
        DFS(L + 1, total + G[L])
        DFS(L + 1, total - G[L])
        DFS(L + 1, total)


@judge()
def solve():
    global n, G, s, res
    n = int(input())
    G = list(map(int, input().split()))
    s = sum(G)
    res = set()
    DFS(0, 0)
    return s - len(res)


solve()
