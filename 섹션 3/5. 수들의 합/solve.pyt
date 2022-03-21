import sys


for index in range(1, 6):
    with open(f"in{index}.txt", "rt", encoding="utf8") as sys.stdin:
        n, m = map(int, input().split())
        li = list(map(int, input().split()))

        # 방법 1
        lt = 0
        rt = 1
        tot = li[0]
        cnt = 0
        while True:
            if tot < m:
                if rt < n:
                    tot += li[rt]
                    rt += 1
                else:
                    break
            elif tot == m:
                cnt += 1
                tot -= li[lt]
                lt += 1
            else:
                tot -= li[lt]
                lt += 1

        # 방법2 성능개선필요
        # cnt = 0
        # tot = 0
        # for i, x in enumerate(li):
        #     if tot == m:
        #         cnt += 1
        #     tot = x
        #     for y in li[i + 1 :]:
        #         if tot < m:
        #             tot += y
        #         elif tot == m:
        #             cnt += 1
        #             tot = 0
        #             break
        #         else:
        #             tot = 0
        #             break

        print(cnt)
