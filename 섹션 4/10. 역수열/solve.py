import sys


sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


@judge(1, 2)
def solve():
    n = int(input())
    numbers = list(map(int, input().split()))
    seq = [0] * n
    for i in range(n):
        for j in range(n):
            # 큰수의 카운트가 0이고 시퀀스가 빈 공간일때 => 알맞은 위치 파악
            if numbers[i] == 0 and seq[j] == 0:
                seq[j] = i + 1
                break
            # 큰수의 카운트가 0이 아니고 시퀀스가 빈 공간일때 => 수 앞에 큰 수가 들어감
            elif seq[j] == 0:
                numbers[i] -= 1
            # 두 조건 모두 아닐때 반복문이 돌며 시퀀스 !위치만! 이동

    return seq


solve()
