import sys


def digit_sum(number):
    result = 0
    for i in number:
        result += int(i)
    return result


for index in range(1, 6):
    with open(f"in{index}.txt", "rt", encoding="utf8") as sys.stdin:
        n = input()
        k = list(input().split())
        li = []
        for x in k:
            li.append(digit_sum(x))
        idx = li.index(max(li))
        print(k[idx])
