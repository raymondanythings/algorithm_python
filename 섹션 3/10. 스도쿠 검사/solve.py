import sys


sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


def check(a):
    for i in range(9):
        ch1 = [0] * 10
        ch2 = [0] * 10
        for j in range(9):
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False
    for i in range(3):
        for j in range(3):
            ch3 = [0] * 10
            for k in range(3):
                for s in range(3):
                    ch3[a[i * 3 + k][j * 3 + s]] = 1
            if sum(ch3) != 9:
                return False
    return True


@judge()
def solve():
    li = [list(map(int, input().split())) for _ in range(9)]

    # 방법 1

    # col = [[] for _ in range(9)]
    # box = [[] for _ in range(9)]
    # for page, x in enumerate(li):
    #     if len(set(x)) != 9:
    #         return "NO"
    #     for i in range(3):
    #         box[((page // 3) * 3) + i] += x[i * 3 : i * 3 + 3]
    #     for j in range(9):
    #         col[j].append(x[j])
    # for x in col:
    #     if len(set(x)) != 9:
    #         return "NO"
    # for x in box:
    #     if len(set(x)) != 9:
    #         return "NO"
    # return "YES"

    # 방법 2

    if check(li):
        return "YES"
    return "NO"


solve()
