from collections import deque
import sys
import os

sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


@judge()
def solve():
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(k)]
    ch = [[0] * n for _ in range(k)]
    Q = deque()
    for i in range(k):
        for j in range(n):
            if board[i][j] == 1:
                Q.append((i, j))
    while Q:
        tmp = Q.popleft()
        for m in range(4):
            x = tmp[0] + dx[m]
            y = tmp[1] + dy[m]
            if 0 <= x < k and 0 <= y < n and board[x][y] == 0:
                ch[x][y] = ch[tmp[0]][tmp[1]] + 1
                board[x][y] = 1
                Q.append((x, y))
    res = 0
    for x in ch:
        if res < (mv := max(x)):
            res = mv
    for y in board:
        if 0 in y:
            res = -1
            break
    return res


solve()
