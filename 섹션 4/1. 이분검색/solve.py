import sys
import os


if os.name == 'nt':
    sys.path.insert(0, "\\".join(os.getcwd().split("\\")[:-2]))
else:
    sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge


@judge()
def solve():
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    li.sort()
    # for i in range(n):
    #     if li[i] == m:
    #         return i + 1

    lt = 0
    rt = n - 1
    while lt <= rt:
        mid = (lt + rt) // 2
        if li[mid] == m:
            return mid + 1
        elif li[mid] > m:
            rt = mid - 1
        else:
            lt = mid + 1


solve()
