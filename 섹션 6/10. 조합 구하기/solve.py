import sys
import os

sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge


def DFS(L, s):
    global cnt, result
    if L == m:
        re = []
        for j in range(L):
            re.append(res[j])
        cnt += 1
        result.append(re)
        re = []
    else:
        for i in range(s, n + 1):
            res[L] = i
            DFS(L + 1, i + 1)


@judge()
def solve():
    global m, res, cnt, n, result
    n, m = map(int, input().split())
    res = [0] * (n + 1)
    cnt = 0
    result = []
    DFS(0, 1)
    return "".join((map(lambda x: " ".join(map(str, x)), result))) + str(cnt)


solve()
