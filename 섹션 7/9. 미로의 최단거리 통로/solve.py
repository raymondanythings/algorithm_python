from collections import deque
import sys
import os

sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge


@judge()
def solve():
    board = [list(map(int, input().split())) for _ in range(7)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dis = [[0] * 7 for _ in range(7)]
    Q = deque()
    Q.append((0, 0))
    board[0][0] = 1
    result = 0
    while Q:
        tmp = Q.popleft()
        for i in range(4):
            x = tmp[0] + dx[i]
            y = tmp[1] + dy[i]
            if 0 <= x <= 6 and 0 <= y <= 6 and not board[x][y]:
                board[x][y] = 1
                dis[x][y] = dis[tmp[0]][tmp[1]] + 1
                Q.append((x, y))
    if not dis[6][6]:
        result = -1
    else:
        result = dis[6][6]
    return result


solve()
