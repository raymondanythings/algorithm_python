import sys


sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


def DFS(L):
    if k == L:
        result.append(tuple(res))
        return
    else:
        for i in range(1, n + 1):
            if ar[i] == 0:
                ar[i] = 1
                res[L] = i
                DFS(L + 1)
                ar[i] = 0


@judge()
def solve():
    global n, k, ar, res, result
    n, k = map(int, input().split())
    ar = [0] * (n + 1)
    res = [0] * k
    result = []
    DFS(0)

    return "".join(map(lambda x: " ".join(map(str, x)), result)) + str(len(result))


solve()
