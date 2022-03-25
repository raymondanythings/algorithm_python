import sys


sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


@judge()
def solve():
    n = int(input())

    # 방법 1

    # data = dict((input(), 1) for _ in range(n))
    # for _ in range(n - 1):
    #     t = input()
    #     if t in data.keys():
    #         del data[t]
    # return list(data.keys())[0]

    # 방법 2

    p = dict()
    for _ in range(n):
        word = input()
        p[word] = 1

    for _ in range(n - 1):
        word = input()
        p[word] = 0

    for key, val in p.items():
        if val == 1:
            return key


solve()
