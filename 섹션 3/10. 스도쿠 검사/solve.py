import sys
import os


if os.name == 'nt':
    sys.path.insert(0, "\\".join(os.getcwd().split("\\")[:-2]))
else:
    sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge


@judge()
def solve():
    board = [list(map(int, input().split())) for _ in range(9)]

    for i in range(9):
        ch1 = [0] * 10
        ch2 = [0] * 10
        for j in range(9):
            if ch1[board[i][j]] == 0:
                ch1[board[i][j]] = 1
            else:
                return 'NO'
            if ch2[board[j][i]] == 0:
                ch2[board[j][i]] = 1
            else:
                return 'NO'
    for i in range(3):
        for j in range(3):
            ch = [0] * 10
            for x in range(3):
                for y in range(3):
                    if ch[board[x + i * 3][y + j * 3]] == 0:
                        ch[board[x + i * 3][y + j * 3]] = 1
                    else:
                        return 'NO'

    return 'YES'


solve()
