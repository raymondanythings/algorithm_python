import sys


def digit_sum(number):
    result = 0
    for i in str(number):
        result += int(i)
    return result


def digit_sum2(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return sum


for index in range(1, 6):
    with open(f"in{index}.txt", "rt", encoding="utf8") as sys.stdin:
        n = input()
        k = list(map(int, input().split()))
        li = []
        mx = -1
        for x in k:
            data = digit_sum(x)
            li.append(data)
            if data > mx:
                mx = data
                res = x
        idx = li.index(max(li))
        print(k[idx])
        print(res)
