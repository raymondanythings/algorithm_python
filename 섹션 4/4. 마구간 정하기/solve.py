import sys


sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


@judge()
def solve():
    def Count(mid):
        cnt = 1
        ep = li[0]
        for i in range(1, n):
            if li[i] - ep >= mid:
                cnt += 1
                ep = li[i]
        return cnt

    n, k = map(int, input().split())
    li = list(int(input()) for _ in range(n))
    li.sort()
    lt = li[0]
    rt = li[-1]

    # 방법 1

    # while lt <= rt:
    #     mid = (lt + rt) // 2
    #     cnt = 1
    #     ep = li[0]
    #     for x in range(1, n):
    #         if li[x] - ep >= mid:
    #             cnt += 1
    #             ep = li[x]
    #     if cnt >= k:
    #         res = mid
    #         lt = mid + 1
    #     else:
    #         rt = mid - 1

    #  방법 2

    while lt <= rt:
        mid = (lt + rt) // 2
        if Count(mid) >= k:
            res = mid
            lt = mid + 1
        else:
            rt = mid - 1

    print(res)
    return res


solve()
