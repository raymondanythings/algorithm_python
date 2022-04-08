import sys
import os

sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge


def DFS(L, total):
    global T, k, cv, cn, cnt
    if total > T:
        return
    if L == k:
        if total == T:
            cnt += 1
    else:
        for i in range(cn[L] + 1):
            DFS(L + 1, total + cv[L] * i)


@judge()
def solve():
    global T, k, cv, cn, cnt
    T = int(input())
    k = int(input())
    cv = []
    cn = []
    for _ in range(k):
        a, b = map(int, input().split())
        cv.append(a)
        cn.append(b)
    cnt = 0
    DFS(0, 0)
    return cnt


solve()
