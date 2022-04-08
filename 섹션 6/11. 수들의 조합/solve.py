import sys
import os

import itertools as it

sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge


def DFS(L, s, sum):
    global cnt
    if L == k:
        if sum % m == 0:
            cnt += 1
        return
    else:
        for i in range(s, n):
            DFS(L + 1, i + 1, sum + li[i])


@judge()
def solve():
    global n, m, li, k, cnt
    n, k = map(int, input().split())
    li = list(map(int, input().split()))
    m = int(input())
    cnt = 0

    # 재귀함수를 활용한 풀이
    # DFS(0, 0, 0)

    # 라이브러리(itertools) 활용한 풀이

    for x in it.combinations(li, k):
        if sum(x) % m == 0:
            cnt += 1

    return cnt


solve()
