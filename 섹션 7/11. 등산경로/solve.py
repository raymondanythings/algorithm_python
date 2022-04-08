import sys
import os

sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(s, e):
    global n, board, cnt, mx
    if board[s][e] == mx:
        cnt += 1
    else:
        for i in range(4):
            x = s + dx[i]
            y = e + dy[i]
            if 0 <= x < n and 0 <= y < n and board[s][e] < board[x][y]:
                DFS(x, y)


@judge()
def solve():
    global n, board, cnt, mx, mn
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    cc = 0
    mn = float("inf")
    mx = float("-inf")
    sx = 0
    sy = 0
    for j, i in enumerate(board):
        if mn > (sm := min(i)):
            mn = sm
            sx = j
            sy = i.index(sm)
        if mx < (em := max(i)):
            mx = em
    DFS(sx, sy)
    return cnt


solve()
