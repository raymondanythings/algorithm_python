import sys
import os

sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge


def DFS(v):
    global cnt, path
    if v == n:
        print(path)
        cnt += 1
    else:
        for i in range(1, n + 1):
            if g[v][i] and not ch[i]:
                ch[i] = 1
                path.append(i)
                DFS(i)
                path.pop()
                ch[i] = 0


@judge(1, 2)
def solve():
    global n, m, g, ch, cnt, path
    n, m = map(int, input().split())
    g = [[0] * (n + 1) for _ in range(n + 1)]
    ch = [0] * (n + 1)
    for i in range(m):
        (
            a,
            b,
        ) = map(int, input().split())
        g[a][b] = 1
    print(g)
    ch[1] = 1
    path = []
    path.append(1)
    cnt = 0
    DFS(1)
    return cnt


solve()
