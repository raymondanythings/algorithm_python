import sys


def calc(num: int, value: int) -> int:
    if num == 1:
        return value * 100
    elif num == 2:
        return 1000 + value * 100
    return 10000 + value * 1000


for index in range(1, 6):
    with open(f"in{index}.txt", "rt", encoding="utf8") as sys.stdin:
        N = int(input())

        # 방법 1

        # res = 0
        # for i in range(N):
        #     tmp = input().split()
        #     tmp.sort()
        #     a, b, c = map(int, tmp)
        #     if a == b and b == c:
        #         money = 10000 + a * 1000
        #     elif a == b or a == c:
        #         money = 1000 + (a * 100)
        #     elif b == c:
        #         money = 1000 + (b * 100)
        #     else:
        #         money = c * 100
        #     if money > res:
        #         res = money
        # print(res)

        # 방법 2

        result = []
        for i in range(N):
            member = list(map(int, input().split()))
            re = 0
            for x in member:
                number = member.count(x)
                if number != 1:
                    re = calc(number, x)
                else:
                    re = calc(1, max(member))
                result.append(re)
        print(max(result))
