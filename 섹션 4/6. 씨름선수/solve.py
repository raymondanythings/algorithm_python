import sys


sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


@judge()
def solve():
    n = int(input())
    members = [list(map(int, input().split())) for _ in range(n)]
    members.sort(reverse=True)
    cnt = 0
    ep = 0
    for _, w in members:
        if w > ep:
            cnt += 1
            ep = w

    return cnt


solve()
