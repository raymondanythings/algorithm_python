from collections import deque
import sys


sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


@judge()
def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    nums = deque(nums)
    q = []
    last = 0
    lt = 0
    rt = n - 1
    res = ""
    while True:
        if last < nums[lt]:
            q.append((nums[lt], "L"))
        if last < nums[rt]:
            q.append((nums[rt], "R"))
        q.sort()
        if len(q) == 0:
            break
        else:
            res += q[0][1]
            last = q[0][0]
            if q[0][1] == "L":
                lt += 1
            else:
                rt -= 1
        q.clear()
    return str(len(res)) + res


"""
2 4 5 1 3

2

4 5 1 3

2 3

4 5 1



"""
solve()
