import sys
import heapq as hq

sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


@judge()
def solve():

    # 방법 1

    """
    heapq 묘듈 => 최소힙기준으로 매소드 사용

    """

    result = ""
    a = []
    while True:
        n = int(input())
        if n == -1:
            break

        if n == 0:
            if len(a) == 0:
                result += "-1"
            else:
                result += str(hq.heappop(a))
        else:
            hq.heappush(a, n)
    return result


solve()
