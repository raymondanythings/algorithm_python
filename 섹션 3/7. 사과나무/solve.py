import sys
import os


if os.name == 'nt':
    sys.path.insert(0, "\\".join(os.getcwd().split("\\")[:-2]))
else:
    sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge


@judge()
def solve():

    # solve 1

    # n = int(input())
    # arr = [list(map(int, input().split())) for _ in range(n)]
    # answer = 0
    # for i in range(n):
    #     s = abs(n // 2 - i)
    #     l = n - s
    #     answer += sum(arr[i][s:l])
    # return answer

    # solve 2
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    s = e = n // 2
    for i in range(n):
        for j in range(s, e+1):
            answer += arr[i][j]
        if i < n // 2:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1
    return answer


solve()
'''
7 7 7 7 7 7 7

3 3 3 3 3 3 3
0 1 2 3 4 5 6
3 2 1 0 1 2 3



'''
