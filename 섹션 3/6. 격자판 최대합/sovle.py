import sys

sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


@judge
def solve():
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    # 방법 1

    largest = -1

    for i in range(n):
        sum1 = sum2 = 0
        for j in range(n):
            sum1 += li[i][j]
            sum2 += li[j][i]
        if sum1 > largest:
            largest = sum1
        if sum2 > largest:
            largest = sum2

    sum1 = sum2 = 0
    for i in range(n):
        sum1 += li[i][i]
        sum2 += li[i][n - i - 1]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

    # 방법 2

    row = col = crs1 = crs2 = []
    for i in range(n):
        row.append(sum(li[i]))
        ar = 0
        for j in range(n):
            ar += li[j][i]
        col.append(ar)
    crs1 += [li[i][i]]
    crs2 += [li[i][n - i - 1]]
    result = list(map(max, [row, col, crs1, crs2]))
    return max(result)


solve()
