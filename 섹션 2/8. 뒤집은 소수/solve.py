import sys


def reverse(number: int) -> int:
    st = int(str(number)[::-1].lstrip("0"))
    res = 0

    # 정수형 계산법
    while number > 0:
        t = number % 10
        res = res * 10 + t
        number = number // 10
    # 1 // 10 => 0
    return st


def is_prime(number: int) -> bool:
    if number == 1:
        return False
    for i in range(
        2, number // 2 + 1
    ):  # 약수는 1X자기자신 ex) 15 => 1 X 15  따라서 2부터 시작하기때문에 2X자기자신 //2 가 최소값
        if number % i == 0:
            return False
    return True


for index in range(1, 6):
    with open(f"in{index}.txt", "rt", encoding="utf8") as sys.stdin:
        n = int(input())
        arr = list(map(int, input().split()))
        for x in arr:
            tmp = reverse(x)
            if is_prime(tmp):
                print(tmp, end=" ")
        print()
