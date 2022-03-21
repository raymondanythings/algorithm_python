import sys


sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


@judge()
def solve():
    n, k = map(int, input().split())
    li = list(map(int, input().split()))
    li.sort()

    # 방법 1
    # return li.index(k) + 1

    # 방법 2 -> 이분탐색 => 바이너리 서치 ** 중요 **

    """
    * 바이너리서치

    lt = 리스트 시작점 선택자
    rt = 리스트 마지막점 선택자
    mid = 전체 리스트 크기의 중간 선택자 ==> (lt + rt) // 2
    """
    lt = 0
    rt = n - 1
    while True:
        mid = (lt + rt) // 2
        if li[mid] > k:
            rt = mid - 1
        elif li[mid] < k:
            lt = mid + 1
        else:
            return mid + 1


solve()
