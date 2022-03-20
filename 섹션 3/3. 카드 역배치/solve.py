import sys


for index in range(1, 6):
    with open(f"in{index}.txt", "rt", encoding="utf8") as sys.stdin:
        cards = list(range(1, 21))
        for _ in range(10):
            ai, bi = map(lambda x: x - 1, map(int, input().split()))
            shuffled = cards[ai : bi + 1]
            del cards[ai : bi + 1]
            for i in shuffled:
                cards.insert(ai, i)

            # 방법 2
            # for i in range((bi - ai + 1) // 2):
            #     cards[ai + i], cards[bi - i] = cards[bi - i], cards[ai + i]

        a = lambda x: print(x, end=" ")
        for x in cards:
            a(x)
        print()
