import sys


sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


@judge()
def solve():
    n = input()
    stack = []
    res = ""
    for i in n:
        if i.isdecimal():
            res += i
        else:
            if i == "(":
                stack.append(i)
            elif i in ("*", "/"):
                while stack and (stack[-1] == "*" or stack[-1] == "/"):
                    res += stack.pop()
                stack.append(i)
            elif i in ("+", "-"):
                while stack and stack[-1] != "(":
                    res += stack.pop()
                stack.append(i)
            elif i == ")":
                while stack and stack[-1] != "(":
                    res += stack.pop()
                stack.pop()
    while stack:
        res += stack.pop()

    return res


solve()
