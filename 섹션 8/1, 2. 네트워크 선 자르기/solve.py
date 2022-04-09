import sys
import os

sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge


# def DFS(L, cnt):
#     global n, re
#     if cnt > n:
#         return
#     elif cnt == n:
#         re += 1
#     else:
#         DFS(L + 1, cnt + 1)
#         DFS(L + 1, cnt + 2)


@judge()
def solve():
    global n, re
    n = int(input())
    re = 0

    dy = [0] * (n + 1)
    dy[1] = 1
    dy[2] = 2
    for i in range(3, n + 1):
        dy[i] = dy[i - 1] + dy[i - 2]
    re = dy[-1]
    # DFS(0, 0)
    # print(re)
    return re


solve()
