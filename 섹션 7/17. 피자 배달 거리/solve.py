from glob import glob
import sys
import os

sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge


def DFS(L, s):
    global n, m, board, hs, pz, cb, res
    if L == m:
        sum = 0
        for j in range(len(hs)):
            x1 = hs[j][0]
            y1 = hs[j][1]
            dis = float("inf")
            for x in cb:
                x2 = pz[x][0]
                y2 = pz[x][1]
                dis = min(dis, abs(x1 - x2) + abs(y1 - y2))
            sum += dis
        print(sum, res)
        if sum < res:
            res = sum
    else:
        for i in range(s, len(pz)):
            cb[L] = i
            DFS(L + 1, i + 1)


@judge(1, 2)
def solve():
    global n, m, board, hs, pz, cb, res
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    hs = []
    pz = []
    cb = [0] * m
    res = float("inf")
    for i in range(n):
        for j in range(n):
            if (lo := board[i][j]) == 1:
                hs.append((i, j))
            elif lo == 2:
                pz.append((i, j))
    DFS(0, 0)
    print(res)
    return res


solve()
