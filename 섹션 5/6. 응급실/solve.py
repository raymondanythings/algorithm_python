import sys
from collections import deque

sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


@judge()
def solve():
    m, k = map(int, input().split())
    dq = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
    dq = deque(dq)

    cnt = 0

    while True:
        tmp = dq.popleft()
        if any(tmp[1] < x[1] for x in dq):
            dq.append(tmp)
        else:
            cnt += 1
            if tmp[0] == k:
                break
    return cnt


solve()
