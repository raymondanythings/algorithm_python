# import sys


# # 에라토스테네스 체
# for index in range(1, 6):
#     with open(f"in{index}.txt", "rt", encoding="utf8") as sys.stdin:
#         n = int(input())
#         arr = [0] * (n + 1)
#         primes = []
#         for i in range(2, n + 1):
#             if arr[i] == 0:
#                 primes.append(i)
#                 for j in range(i, n + 1, i):
#                     arr[j] = 1
#         print(len(primes))
import sys

sys.path.append("C:/Users/user/Documents/algorithm_python")
from judge import judge


@judge()
def solve():
    answer = 0
    n = int(input())
    checked = [False,False] + [True] * n    
    for i in range(2, n + 1):
        if checked[i]:
            answer += 1
            checked[i] = False
            for j in range(i , n + 1, i):
                checked[j] = False
    
    return answer


solve()