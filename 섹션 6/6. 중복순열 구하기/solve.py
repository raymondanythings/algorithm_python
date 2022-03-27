import sys


sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge

# 2개 이상의 가지를 뻗는방법


def DFS(L):
    global result
    if L == m:
        result.append(tuple(ar))
        return
    else:
        for i in nums:
            ar[L] = i
            DFS(L + 1)


@judge()
def solve():
    global n, m, nums, result, ar
    n, m = map(int, input().split())
    nums = [i + 1 for i in range(n)]
    result = []
    ar = [0] * m
    DFS(0)
    return "".join(map(lambda x: " ".join(map(str, x)), result)) + str(len(result))


solve()
