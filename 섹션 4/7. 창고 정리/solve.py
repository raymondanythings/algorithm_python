import sys
import os


if os.name == 'nt':
    sys.path.insert(0, "\\".join(os.getcwd().split("\\")[:-2]))
else:
    sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge


@judge()
def solve():
    n = int(input())
    boxes = list(map(int, input().split()))
    m = int(input())
    for _ in range(m):
        top = boxes.index(max(boxes))
        bottom = boxes.index(min(boxes))
        boxes[top] -= 1
        boxes[bottom] += 1
    return max(boxes) - min(boxes)


solve()
