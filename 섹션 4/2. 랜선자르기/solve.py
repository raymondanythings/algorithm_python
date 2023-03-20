import sys
import os


if os.name == 'nt':
    sys.path.insert(0, "\\".join(os.getcwd().split("\\")[:-2]))
else:
    sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge


@judge()
def solve():
    K, N = map(int, input().split())
    lines = [int(input()) for _ in range(K)]
    lt = 0
    rt = max(lines)
    while lt <= rt:
        mid = (lt+rt) // 2
        cnt = 0
        for line in lines:
            cnt += line // mid
        if cnt < N:
            rt = mid - 1
        else:
            lt = mid + 1
    return mid


solve()
