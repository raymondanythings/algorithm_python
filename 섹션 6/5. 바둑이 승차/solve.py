import sys


sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


def DFS(L, sum, tsum):
    global result
    # cut Edge Tech -> DFS가 순환할때, 목표값 이상 또는 이하인 부분집합 생략함으로
    # 처리속도 향상
    if sum + (total - tsum) < result:
        return
    if sum > w:
        return
    if L == n:
        if sum > result:
            result = sum
    else:
        DFS(L + 1, sum + dogs[L], tsum + dogs[L])
        DFS(L + 1, sum, tsum + dogs[L])


@judge()
def solve():
    global n
    global w
    global dogs
    global result
    global total

    result = -100
    w, n = map(int, input().split())
    dogs = [int(input()) for _ in range(n)]
    total = sum(dogs)
    DFS(0, 0, 0)

    return result


solve()
