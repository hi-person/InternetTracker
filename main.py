import requests
from time import time, sleep
from os import system
from datetime import datetime
x = 0
a = 0
w = str(datetime.now())[8:10]
while True:
    try:
        c = time()
        requests.head("https://www.bing.com/", timeout=5000)
        x += time() - c + 3
        if int(str(datetime.now())[8:10]) != int(w):
            system("cls")
            x = 0
            a = 0
        w = str(datetime.now())[8:10]
    except requests.ConnectionError:
        pass
    if a != x:
        y = divmod(round(x), 60)
        z = divmod(y[0], 60)
        print(f"{z[0]}:{z[1]}:{y[1]}")
        a = x
    sleep(3)
