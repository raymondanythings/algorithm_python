from collections import deque
import sys
import os

sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


@judge()
def solve():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    Q = deque()
    cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                Q.append((i, j))
                board[i][j] = 0
                while Q:
                    tmp = Q.popleft()
                    for m in range(8):
                        x = tmp[0] + dx[m]
                        y = tmp[1] + dy[m]
                        if 0 <= x < n and 0 <= y < n and board[x][y]:
                            board[x][y] = 0
                            Q.append((x, y))
                cnt += 1
    return cnt


solve()
