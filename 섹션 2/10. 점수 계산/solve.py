import sys

sys.path.append("C:/Users/user/Documents/algorithm_python")
from judge import judge
from collections import deque

@judge()
def solve():
    answer =0
    n = int(input())
    r = list(map(int,input().split()))
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
