import sys


sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


def DFS(L, sum):
    global result
    if sum > total // 2:
        return
    if L == n:
        if sum == (total - sum):
            result = "YES"
            return
    else:
        DFS(L + 1, sum + nums[L])
        DFS(L + 1, sum)


@judge()
def solve():
    global n
    global result
    global total
    global nums
    result = "NO"

    n = int(input())
    nums = list(map(int, input().split()))
    total = sum(nums)
    DFS(0, 0)

    return result


solve()
