import sys
import os

sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge


def DFS(L, salary):
    global res, T, P, n
    if L > n + 1:
        return
    if L == n + 1:
        if salary > res:
            res = salary
    else:
        DFS(L + T[L - 1], salary + P[L - 1])
        DFS(L + 1, salary)


@judge()
def solve():
    global n, T, P, res
    n = int(input())
    T = []
    P = []
    for _ in range(n):
        a, b = map(int, input().split())
        T.append(a)
        P.append(b)
    res = float("-inf")
    DFS(1, 0)
    return res


solve()
