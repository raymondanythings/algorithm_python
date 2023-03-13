import sys

sys.path.append("C:/Users/user/Documents/algorithm_python")
from judge import judge


@judge()
def solve():
    n = int(input())
    answer = ''
    for i in range(n):
        N,s,e,k = map(int,input().split())
        li = list(map(int,input().split()))[s-1:e]
        li.sort()
        answer += f'#{i+1} {li[k-1]}'
    return answer


solve()
