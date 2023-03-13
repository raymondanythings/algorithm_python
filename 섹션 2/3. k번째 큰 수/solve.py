import sys

sys.path.append("C:/Users/user/Documents/algorithm_python")
from judge import judge


@judge()
def solve():
    N , K = map(int,input().split())
    cards = list(map(int,input().split()))
    re = set()
    for i in range(N):
        for j in range(i + 1, N):
            for m in range(j + 1, N):
                re.add(cards[i] + cards[j] + cards[m])
    result = list(re)
    result.sort(reverse=True)
    return result[K -1]


solve()
