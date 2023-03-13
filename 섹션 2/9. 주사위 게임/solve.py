import sys

sys.path.append("C:/Users/user/Documents/algorithm_python")
from judge import judge


@judge()
def solve():
    answer = 0
    n = int(input())
    for i in range(n):
        re = list(map(int,input().split()))
        tmp = set(re)
        score = 0
        if len(tmp) == 3:
            score = 100 + max(re) * 100
        elif len(tmp) == 1:
            score = 10000 + re[0] * 1000
        else:
            for j in re:
                c = re.count(j)
                if c == 2:
                    score = 1000 + j * 100
                    break
        if answer < score:
            answer = score
    return answer


solve()