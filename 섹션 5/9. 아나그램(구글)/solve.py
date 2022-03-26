import sys


sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


@judge()
def solve():
    t_word = input()
    c_word = input()

    a_dic = dict()
    b_dic = dict()
    result = "NO"

    # 방법 1

    # t_set_word = set(t_word)
    # for i in t_set_word:
    #     a_dic[i] = t_word.count(i)
    #     b_dic[i] = c_word.count(i)

    # if a_dic == b_dic:
    #     result = "YES"

    # 방법 2

    # for x in t_word:
    #     a_dic[x] = a_dic.get(x, 0) + 1
    # for x in c_word:
    #     b_dic[x] = b_dic.get(x, 0) + 1

    # for i in a_dic.keys():
    #     if i in b_dic.keys():
    #         if a_dic[i] != b_dic[i]:
    #             break
    #     else:
    #         break
    # else:
    #     result = "YES"

    # 방법 3

    str1 = [0] * 52
    str2 = [0] * 52

    for x in t_word:
        if x.isupper():
            str1[ord(x) - 65] += 1
        else:
            str1[ord(x) - 71] += 1

    for x in c_word:
        if x.isupper():
            str2[ord(x) - 65] += 1
        else:
            str2[ord(x) - 71] += 1

    # if str1 == str2:
    #     result = "YES"

    for i in range(52):
        if str1[i] == str2[i]:
            result = "YES"
            break

    return result


solve()
