import random
import time

i = 0
while i <10:
    load = random.randint(0,100)
    if load > 85:
        print(f"Крылышки в опасности! Нагрузка: {load} ")
    time.sleep(0.2)
    i +=1
