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

    lt = 0
    rt = 1
    tot = li[0]
    cnt = 0
    while True:
        if tot == m:
            cnt += 1
            tot -= li[lt]
            lt += 1
        elif tot < m:
            if rt >= n:
                break
            else:
                tot += li[rt]
                rt += 1
        else:
            tot -= li[lt]
            lt += 1
    print(lt)
    return cnt


solve()
