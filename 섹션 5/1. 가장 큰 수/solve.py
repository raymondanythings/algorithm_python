import sys


sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


@judge()
def solve():
    numbers, k = list(map(int, input().split()))
    numbers = list(map(int, str(numbers)))

    # 방법 1

    stack = [numbers[0]]
    for x in numbers[1:]:
        for i in stack[::-1]:
            if k == 0:
                break
            if i < x:
                stack.pop()
                k -= 1
        stack += [x]
    if k > 0:
        stack = stack[:-k]
    txt = "".join(map(str, stack))

    # 방법 2

    # stack = []
    # for x in numbers:
    #     while stack and k > 0 and stack[-1] < x:
    #         stack.pop()
    #         k -= 1
    #     stack += [x]
    # if k > 0:
    #     stack = stack[:-k]
    # txt = "".join(map(str, stack))
    return txt


solve()
