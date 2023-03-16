import sys
import os
import math
import time


def judge(start=1, end=6):
    def set_deco(func):
        def wrapper():
            for index in range(start, end):
                print(os.getcwd())
                start_time = time.time()
                with open(f"{os.getcwd()}/in{index}.txt", "rt", encoding="utf8") as sys.stdin:
                    result = func()
                    if isinstance(result, list):
                        txt = ""
                        for x in result:
                            txt += f"{x} "
                        result = txt.strip()
                    else:
                        result = str(result)
                with open(f"{os.getcwd()}/out{index}.txt", "rt", encoding="utf8") as re:
                    current = re.read().replace("\n", "")
                    txt = f"Case #{index} : "
                    print("CURRENT : ", current)
                    print("ANSWER : ", result)
                    if result == current:
                        print(txt, "Clear!")
                    else:
                        print(txt, "Error!")
                end_time = time.time()
                print(f'TIME: {end_time - start_time: .8f} sec \n')
            return

        return wrapper

    return set_deco
