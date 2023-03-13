import sys

sys.path.append("C:/Users/user/Documents/algorithm_python")
from judge import judge


@judge()
def solve():
    n = int(input())
    scores = list(map(int,input().split()))
    avg = round(sum(scores) / n)
    m = float('inf')
    idx = 0
    for i ,score in enumerate(scores):
        tmp = abs(avg - score)
        if tmp < m:
            m = tmp
            s = score
            idx = i + 1
        elif tmp == avg:
            if score > s:
                s = score
                idx = i + 1
    return f'{avg} {idx}'


solve()



