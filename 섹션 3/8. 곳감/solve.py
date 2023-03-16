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
    arr = [list(map(int, input().split())) for _ in range(n)]

    m = int(input())

    for _ in range(m):
        row, direction, time = map(int, input().split())
        target = arr[row-1].copy()
        for i, t in enumerate(target):
            if direction == 0:
                arr[row-1][(i - time) % n] = t
            else:
                arr[row-1][(i + time) % n] = t
    for j in range(n):
        middle = n // 2
        s = abs(abs(middle - j) - middle)
        l = n - s
        answer += sum(arr[j][s:l])

    return answer


# @judge()
# def solve():
#     n = int(input())
#     a = [list(map(int, input().split())) for _ in range(n)]
#     m = int(input())
#     for i in range(m):
#         h, t, k = map(int, input().split())
#         if t == 0:
#             for _ in range(k):
#                 a[h-1].append(a[h-1].pop(0))
#         else:
#             for _ in range(k):
#                 a[h-1].insert(0, a[h-1].pop())
#     res = 0
#     s = 0
#     e = n-1
#     for i in range(n):
#         for j in range(s, e+1):
#             res += a[i][j]
#         if i < n // 2:
#             s += 1
#             e -= 1
#         else:
#             s -= 1
#             e += 1
#     return res


solve()
'''
5 5 5 5 5
2 2 2 2 2

0 1 2 3 4
0 1 2 1 0

2 - 0 - 2 = 0
abs(abs(2 - 1) - 2) = 1
abs(abs(2 - 2) - 2) = 2
abs(abs(2 - 3) - 2) = 1
2 - 4 - 2 = -4

abs(n // 2 - 1) - n // 2
'''
