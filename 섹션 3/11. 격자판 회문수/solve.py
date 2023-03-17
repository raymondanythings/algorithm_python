import sys
import os


if os.name == 'nt':
    sys.path.insert(0, "\\".join(os.getcwd().split("\\")[:-2]))
else:
    sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge


@judge()
def solve():
    answer = 0
    board = [list(map(int, input().split())) for _ in range(7)]
    for i in range(7):
        for j in range(3):
            row = board[i][j:j+5]
            if row[0] == row[4] and row[1] == row[3]:
                answer += 1
    for i in range(7):
        for j in range(3):
            col = [board[j+x][i] for x in range(5)]
            if col[0] == col[4] and col[1] == col[3]:
                answer += 1

    return answer
# @judge()
# def solve():
#     answer = 0
#     board = [list(map(int, input().split())) for _ in range(7)]
#     for i in range(3):
#         for j in range(7):
#             tmp = board[j][i:i+5]
#             if tmp == tmp[::-1]:
#                 answer += 1
#             for k in range(2):
#                 if board[i+k][j] != board[i+5-k-1][j]:
#                     break
#             else:
#                 answer += 1

#     return answer


solve()
