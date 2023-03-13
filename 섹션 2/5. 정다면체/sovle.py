import sys

sys.path.append("C:/Users/user/Documents/algorithm_python")
from judge import judge


@judge()
def solve():
    n = list(map(int,input().split()))
    return ' '.join(str(x) for x in range(min(n) + 1, max(n) + 2))


solve()

'''
6 : 1 2 3 4 5 6

4 : 1 2 3 4


5 - 10
4 - 9
3 - 8
2 - 7
'''