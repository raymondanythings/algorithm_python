import sys
import os


def judge(func):
    def wrapper():
        file_list = os.listdir(os.getcwd())
        li = []
        for x in file_list:
            if ".txt" in x:
                li.append(x)
        for i in range(1, int(len(li) / 2) + 1):
            with open(f"in{i}.txt", "rt", encoding="utf8") as sys.stdin:
                result = func()
                with open(f"out{i}.txt", "rt", encoding="utf8") as re:
                    current = int(re.read())
                    txt = f"Case #{i} : "
                    if result == current:
                        print(txt, "Clear!")
                    else:
                        print(txt, "Error!")

    return wrapper
