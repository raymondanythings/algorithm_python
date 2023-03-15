import sys
import os


if os.name == 'nt':
    sys.path.insert(0, "\\".join(os.getcwd().split("\\")[:-2]))
else:
    sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge
from collections import deque


@judge()
def solve():
    answer = 0
    n = int(input())
    r = list(map(int, input().split()))
    Q = deque(r)
    s = 0
    while Q:
        score = Q.popleft()
        if score == 0:
            s = 0
        else:
            s += score
            answer += s
    return answer


solve()
