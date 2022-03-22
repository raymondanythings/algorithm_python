import sys


sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


@judge()
def solve():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda x: (x[1], x[0]))

    # 방법 1

    # cnt = 1
    # et = arr[0][1]
    # for i in range(1,n - 1):
    #     if et <= arr[i][0]:
    #         cnt += 1
    #         et = arr[i][1]

    # 방법 2

    et = 0
    cnt = 0
    for s, e in arr:
        if s >= et:
            et = e
            cnt += 1

    return cnt


solve()
