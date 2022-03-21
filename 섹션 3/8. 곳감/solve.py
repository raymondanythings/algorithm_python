import sys

sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


@judge()
def solve():
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    exe_n = int(input())

    # 방법 1
    # exe_list = [list(map(int, input().split())) for _ in range(exe_n)]
    # for row, direction, moved in exe_list:
    #     if moved != 0:
    #         target_list = li[row - 1]
    #         init_list = [0] * n
    #         if not direction:
    #             for i in range(n):
    #                 init_list[i] = target_list[(moved + i) % n]
    #         else:
    #             for i, v in enumerate(target_list):
    #                 init_list[moved] = v
    #                 moved += 1
    #                 if moved >= n:
    #                     moved = 0
    #         li[row - 1] = init_list

    # 방법 2

    for i in range(exe_n):
        h, t, k = map(int, input().split())
        if t == 0:
            for _ in range(k):
                li[h - 1].append(li[h - 1].pop(0))
        else:
            for _ in range(k):
                li[h - 1].insert(0, li[h - 1].pop())

    s, e = 0, n
    result = 0
    for i in range(n):
        result += sum(li[i][s:e])
        if i < n // 2:
            s += 1
            e -= 1
        else:
            s -= 1
            e += 1
    return result


solve()
