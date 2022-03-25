import sys
from collections import deque


sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


@judge()
def solve():
    need = input()
    n = int(input())
    subs = [input() for _ in range(n)]
    result = ""

    # 방법 1

    # q = []
    # ta = list(need)

    # for i, sub in enumerate(subs):
    #     for x in sub:
    #         if x in ta:
    #             q.append(x)
    #         if q == ta:
    #             break
    #     if q == ta:
    #         result += f"#{i + 1} YES"
    #     else:
    #         result += f"#{i + 1} NO"
    #     q = []

    #  방법 2

    for i, sub in enumerate(subs):
        dq = deque(need)
        for x in sub:
            if x in dq:
                print(dq)
                if x != dq.popleft():
                    break
        if not dq:
            result += f"#{i + 1} YES"
        else:
            result += f"#{i + 1} NO"

    return result


solve()
