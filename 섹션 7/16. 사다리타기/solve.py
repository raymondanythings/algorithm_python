import sys
import os

sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge


def DFS(x, y):
    global res
    ch[x][y] = 1
    if x == 0:
        res = y
    else:
        if y - 1 >= 0 and board[x][y - 1] and not ch[x][y - 1]:
            DFS(x, y - 1)
        elif y + 1 < 10 and board[x][y + 1] and not ch[x][y + 1]:
            DFS(x, y + 1)
        else:
            DFS(x - 1, y)


@judge()
def solve():
    global board, ch, res
    board = [list(map(int, input().split())) for _ in range(10)]
    ch = [[0] * 10 for _ in range(10)]
    res = 0
    for i in range(10):
        if board[9][i] == 2:
            DFS(9, i)

    return res


solve()
