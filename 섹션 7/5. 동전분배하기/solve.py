import sys
import os

sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge


def DFS(L):
    global n, l, coins, res
    if L == n:
        if res > (re := max(pe) - min(pe)):
            if len(set(pe)) == 3:
                res = re
    else:
        for i in range(l):
            pe[i] += coins[L]
            DFS(L + 1)
            pe[i] -= coins[L]


@judge()
def solve():
    global n, l, coins, pe, res
    n = int(input())
    l = 3
    pe = [0] * l
    coins = [int(input()) for _ in range(n)]
    res = float("inf")
    DFS(0)
    return res


solve()
