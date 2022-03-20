import sys
import re

for index in range(1, 6):
    with open(f"in{index}.txt", "rt", encoding="utf8") as sys.stdin:
        n = input()

        # 방법 1
        # number = int(re.sub(r"[^0-9]", "", n))
        # cnt = 2
        # for x in range(2, number):
        #     if number % x == 0:
        #         cnt += 1
        # print(f"{number}\n{cnt}\n")

        # 방법 2

        res = 0
        for x in n:
            if x.isdecimal():
                print("x : ", x)
                res = res * 10 + int(x)

        print(res)
        cnt = 0
        for i in range(1, res + 1):
            if res % i == 0:
                cnt += 1
        print(cnt)
