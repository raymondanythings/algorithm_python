import sys


sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


@judge()
def solve():
    brackets = input()
    stack = []
    cnt = 0
    result = 0

    # 방법 1

    for x in brackets:
        if x == "(":
            stack.append(x)
        else:
            stack.pop()
            if brackets[cnt - 1] == "(":
                result += len(stack)
            else:
                result += 1
        cnt += 1

    # 방법 2

    # for i, v in enumerate(brackets):
    #     if v == "(":
    #         stack.append(v)
    #     else:
    #         stack.pop()
    #         if brackets[i - 1] == "(":
    #             result += len(stack)
    #         else:
    #             result += 1

    return result


solve()
