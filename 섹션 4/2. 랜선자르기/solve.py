import sys


sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


@judge()
def solve():
    n, k = map(int, input().split())
    li = [int(input()) for _ in range(n)]
    lt = 1
    rt = max(li)
    res = 0
    while lt <= rt:
        cnt = 0
        mid = (lt + rt) // 2
        for i in li:
            cnt += i // mid
        if cnt >= k:
            res = mid
            lt = mid + 1
        else:
            rt = mid - 1
    return res


solve()
