import sys
import os


if os.name == 'nt':
    sys.path.insert(0, "\\".join(os.getcwd().split("\\")[:-2]))
else:
    sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge


@judge()
def solve():
    n, c = map(int, input().split())
    li = [int(input()) for _ in range(n)]
    li.sort()
    lt = 1
    rt = li[-1]
    res = 0
    while lt <= rt:
        mid = (lt + rt) // 2
        cnt = 1
        h = li[0]
        for i in li[1:]:
            if i - h >= mid:
                cnt += 1
                h = i
        if cnt >= c:
            res = mid
            lt = mid + 1
        else:
            rt = mid - 1
    return res


solve()
