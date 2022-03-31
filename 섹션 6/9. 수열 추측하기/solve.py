import sys


sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


def DFS(L, sum):
    global result, trg
    if not trg:
        return
    if L == n and sum == k:
        if trg:
            result = " ".join(map(str, p)).strip()
            trg = 0
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i
                DFS(L + 1, sum + (p[L] * b[L]))
                ch[i] = 0


@judge()
def solve():
    global n, b, p, ch, k, trg
    n, k = map(int, input().split())
    p = [0] * n
    b = [1] * n
    ch = [0] * (n + 1)
    trg = 1
    for i in range(1, n):
        b[i] = b[i - 1] * (n - i) // i
    DFS(0, 0)
    return result


solve()


"""
1 2 3 4
 3 5 7
  8 12
   20

"""
