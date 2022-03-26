import sys


sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge

"""
재귀함수 => 스택기반으로 실행됨
"""


@judge()
def solve():
    global result
    result = ""
    n = int(input())
    DFS(n)
    return result


def DFS(x):
    global result
    if x == 0:
        return
    DFS(x // 2)
    result += str(x % 2)


if __name__ == "__main__":
    solve()
