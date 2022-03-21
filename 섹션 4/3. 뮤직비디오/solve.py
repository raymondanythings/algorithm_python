import sys


sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


def Count(op, li):
    cnt = 1
    add = 0
    print(f"mid : {op}")
    for x in li:
        if add + x > op:
            print(f"next : {add}")
            cnt += 1
            add = x
        else:
            print(add)
            add += x
    print(f"count : {cnt}")
    return cnt


@judge()
def solve():
    _, k = map(int, input().split())
    li = list(map(int, input().split()))
    maxx = max(li)
    lt = 1
    rt = sum(li)
    res = 0

    # * 핵심 *
    # CD 2장에 저장 가능한 용량은 3장으로도 가능 => k값에 맞추는게 아닌
    # !! 저장 가능한 최소값만 찾으면 됨!!

    # 방법 1
    s = 0
    while lt <= rt:
        cnt = 1
        mid = (lt + rt) // 2
        for x in li:
            if s + x > mid:
                cnt += 1
                s = x
            else:
                s += x
        s = 0
        if mid >= maxx and cnt <= k:
            rt = mid - 1
            res = mid
        else:
            lt = mid + 1

    # 방법 2

    # while lt <= rt:
    #     mid = (lt + rt) // 2
    #     if mid >= maxx and Count(mid, li) <= k:
    #         res = mid
    #         rt = mid - 1
    #     else:
    #         lt = mid + 1

    return res


solve()
