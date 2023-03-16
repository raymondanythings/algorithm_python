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
    n = int(input())
    arr = [[0] * (n + 2)] + [[0] + list(map(int, input().split())) + [0]
                             for _ in range(n)] + [[0] * (n + 2)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            t = arr[i][j]
            if t < arr[i][j - 1]:
                continue
            if t > arr[i-1][j] and t > arr[i][j+1] and t > arr[i+1][j] and t > arr[i][j-1]:
                answer += 1

    return answer

# @judge()
# def solve():
#     dx = [-1, 0, 1, 0]
#     dy = [0, 1, 0, -1]
#     n = int(input())
#     a = [list(map(int, input().split())) for _ in range(n)]
#     a.insert(0, [0] * n)
#     a.append([0] * n)
#     for x in a:
#         x.insert(0, 0)
#         x.append(0)
#     cnt = 0
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if all(a[i][j] > a[i + dx[k]][j + dy[k]] for k in range(4)):
#                 cnt += 1
#     return cnt


solve()
