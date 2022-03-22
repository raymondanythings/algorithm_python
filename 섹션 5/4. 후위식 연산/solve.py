import sys


sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


@judge()
def solve():
    numbers = input()
    stack = []

    for x in numbers:
        if x.isdecimal():
            stack.append(int(x))
        else:
            if x == "+":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n1 + n2)
            elif x == "-":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2 - n1)
            elif x == "*":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2 * n1)
            elif x == "/":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2 - n1)

    return stack.pop()


solve()
