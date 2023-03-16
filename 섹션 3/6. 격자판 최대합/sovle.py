import sys
import os


if os.name == 'nt':
    sys.path.insert(0, "\\".join(os.getcwd().split("\\")[:-2]))
else:
    sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge


@judge()
def solve():
    # n = int(input())
    # li = [list(map(int, input().split())) for _ in range(n)]
    # # 방법 1

    # largest = -1

    # for i in range(n):
    #     sum1 = sum2 = 0
    #     for j in range(n):
    #         sum1 += li[i][j]
    #         sum2 += li[j][i]
    #     if sum1 > largest:
    #         largest = sum1
    #     if sum2 > largest:
    #         largest = sum2

    # sum1 = sum2 = 0
    # for i in range(n):
    #     sum1 += li[i][i]
    #     sum2 += li[i][n - i - 1]
    # if sum1 > largest:
    #     largest = sum1
    # if sum2 > largest:
    #     largest = sum2

    # # 방법 2

    # row = col = crs1 = crs2 = []
    # for i in range(n):
    #     row.append(sum(li[i]))
    #     ar = 0
    #     for j in range(n):
    #         ar += li[j][i]
    #     col.append(ar)
    # crs1 += [li[i][i]]
    # crs2 += [li[i][n - i - 1]]
    # result = list(map(max, [row, col, crs1, crs2]))
    # return max(result)
    n = int(input())
    lagest = -1
    li = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        row = sum(li[i])
        col = sum(li[j][i] for j in range(n))
        if (m_value := max([row, col])) > lagest:
            lagest = m_value
    sum1 = 0
    sum2 = 0
    for x in range(n):
        sum1 += li[x][x]
        sum2 += li[x-n][x-n]
    return max([lagest, sum1, sum2])


solve()
