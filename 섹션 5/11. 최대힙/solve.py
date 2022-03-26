import sys
import heapq as hq

sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


@judge()
def solve():

    """
    파이썬 heaq 모듈은 최대힙 지원 안함
    => 데이터 음수화 하여 최대힙 구현해야함
    """

    a = []
    result = ""

    while True:
        n = int(input())
        if n == -1:
            break

        if n == 0:
            if len(a) == 0:
                result += "-1"
            else:
                result += str(-hq.heappop(a))

        else:
            hq.heappush(a, -n)

    return result


solve()
