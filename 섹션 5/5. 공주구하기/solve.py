import sys
from collections import deque

sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


@judge()
def solve():
    n, k = map(int, input().split())
    li = [i for i in range(1, n + 1)]

    # 방법 1

    # Q = deque(li)
    # cnt = 0
    # while len(Q) > 1:
    #     cnt += 1
    #     tmp = Q.popleft()
    #     if cnt == k:
    #         cnt = 0
    #     else:
    #         Q.append(tmp)
    # return Q[0]

    # 방법 2

    dq = deque(li)
    while dq:
        for _ in range(k - 1):
            cur = dq.popleft()
            dq.append(cur)
        dq.popleft()
        if len(dq) == 1:
            return dq[0]


solve()
