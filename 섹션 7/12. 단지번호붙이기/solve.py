import sys
import os

sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(s, e):
    global n, apt, cnt
    cnt += 1
    apt[s][e] = 0
    for i in range(4):
        x = s + dx[i]
        y = e + dy[i]
        if 0 <= x < n and 0 <= y < n and apt[x][y]:
            DFS(x, y)


@judge()
def solve():
    global n, apt, cnt
    n = int(input())
    apt = [list(map(int, input())) for _ in range(n)]
    res = []
    for i in range(n):
        for j in range(n):
            if apt[i][j]:
                cnt = 0
                DFS(i, j)
                res.append(cnt)
    res.sort()
    res.insert(0, len(res))
    return "".join(map(str, res))


solve()
