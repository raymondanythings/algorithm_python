import sys

sys.path.append("C:/Users/user/Documents/algorithm_python")
from judge import judge


@judge()
def solve():
    n = int(input())
    arr = list(map(int,input().split()))
    answer = 0
    t = 0
    for x in arr:
        s = 0
        for j in str(x):
            s += int(j)
        if s > t:
            t = s
            answer = x
    return answer


solve()