import sys
import os

sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge


def DFS(L, P):
    global n, k, res, cnt, result
    if L >= k:
        q = [y for y in list(map(lambda x: chr(x + 64), res)) if y != "@"]
        result.append("".join(q))
        cnt += 1
    else:
        for i in range(1, 27):
            if i == n[L]:
                res[P] = i
                DFS(L + 1, P + 1)
                res[P] = 0
            elif i >= 10 and n[L] == i // 10 and n[L + 1] == i % 10:
                res[P] = i
                DFS(L + 2, P + 1)
                res[P] = 0


@judge()
def solve():
    global n, k, res, cnt, result
    n = list(map(int, input()))
    k = len(n)
    n.append(k)
    res = [0] * k
    cnt = 0
    result = []
    DFS(0, 0)
    result.append(str(cnt))
    return "".join(result)


solve()
