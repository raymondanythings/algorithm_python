import sys


sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


def DFS(L, s):
    global res
    if L > res:
        return
    if s > target:
        return
    if s == target:
        if L < res:
            res = L
            return
    else:
        for i in range(n):
            DFS(L + 1, s + coins[i])


@judge()
def solve():
    global n, coins, target, res
    n = int(input())
    coins = list(map(int, input().split()))
    target = int(input())
    res = float("inf")
    coins.sort(reverse=True)
    DFS(0, 0)
    return res


solve()
