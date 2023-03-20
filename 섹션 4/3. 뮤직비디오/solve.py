import sys
import os


if os.name == 'nt':
    sys.path.insert(0, "\\".join(os.getcwd().split("\\")[:-2]))
else:
    sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge


@judge()
def solve():
    N, M = map(int, input().split())
    songs = list(map(int, input().split()))
    lt = 1
    rt = sum(songs)
    res = 0
    while lt <= rt:
        mid = (lt + rt) // 2
        cnt = 1
        s = 0
        for i in range(N):
            if s + songs[i] > mid:
                s = songs[i]
                cnt += 1
            else:
                s += songs[i]
        if cnt <= M:
            res = mid
            rt = mid - 1
        else:
            lt = mid + 1
    return res


solve()
