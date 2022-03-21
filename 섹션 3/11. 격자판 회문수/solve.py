import sys


sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


@judge()
def solve():
    board = [list(map(int, input().split())) for _ in range(7)]
    cnt = 0

    # 방법 1
    # for i in range(7):
    #     cols = [board[k][i] for k in range(7)]
    #     for j in range(3):
    #         row = board[i][j : j + 5]
    #         col = cols[j : j + 5]
    #         if row == row[::-1] or col == col[::-1]:
    #             cnt += 1

    # 방법 2
    for i in range(3):
        for j in range(7):
            tmp = board[j][i : i + 5]
            if tmp == tmp[::-1]:
                cnt += 1
            for k in range(2):
                if board[i + k][j] != board[i + 5 - k - 1][j]:
                    break
            else:
                cnt += 1
    return cnt


solve()
