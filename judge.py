import sys
import os


def judge(func):
    def wrapper():
        for index in range(1, 6):
            with open(f"{os.getcwd()}/in{index}.txt", "rt", encoding="utf8") as sys.stdin:
                result = str(func())
            with open(f"{os.getcwd()}/out{index}.txt", "rt", encoding="utf8") as re:
                current = re.read()
                txt = f"Case #{index} : "
                if result == current:
                    print(txt, "Clear!")
                else:
                    print(txt, "Error!")

    return wrapper
