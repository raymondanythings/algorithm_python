import sys


sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


@judge()
def solve():
    n = int(input())
    size = list(map(int, input().split()))
    cycle = int(input())
    size.sort()

    # 방법 1

    for _ in range(cycle):
        max_value = max(size)
        min_value = min(size)
        size[size.index(max_value)], size[size.index(min_value)] = max_value - 1, min_value + 1
    result = max(size) - min(size)

    # 방법 2

    # for _ in range(cycle):
    #     size[0], size[-1] = size[0] + 1, size[-1] - 1
    #     size.sort()
    # result = size[-1] - size[0]

    return result


solve()
