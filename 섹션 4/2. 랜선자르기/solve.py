import sys


sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


@judge()
def solve():
    n, k = map(int, input().split())
    li = [int(input()) for _ in range(n)]

    # 방법 1

    # 바이너리서치 시 lt , rt 최적값 찾기위해 lt <= rt 조건 사용 ==> lt,rt 최소거리일때 최적값
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
