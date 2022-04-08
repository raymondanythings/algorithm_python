from cmath import inf
import sys
import os

sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge


def DFS(L, total, time):
    global res
    if time > m:
        return
    if L == n:
        if total > res:
            res = total
    else:
        DFS(L + 1, total + pv[L], time + pt[L])
        DFS(L + 1, total, time)


@judge()
def solve():
    global n, m, res, pt, pv
    n, m = map(int, input().split())
    pt = []
    pv = []
    for _ in range(n):
        a, b = map(int, input().split())
        pv.append(a)
        pt.append(b)
    res = -inf
    DFS(0, 0, 0)

    return res


solve()
