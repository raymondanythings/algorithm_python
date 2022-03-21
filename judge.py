import sys
import os


def judge(start=1, end=6):
    def set_deco(func):
        def wrapper():
            for index in range(start, end):
                with open(f"{os.getcwd()}/in{index}.txt", "rt", encoding="utf8") as sys.stdin:
                    result = str(func())
                with open(f"{os.getcwd()}/out{index}.txt", "rt", encoding="utf8") as re:
                    current = re.read()
                    txt = f"Case #{index} : "
                    if result == current:
                        print(txt, "Clear!")
                    else:
                        print(txt, "Error!")
            return

        return wrapper

    return set_deco
