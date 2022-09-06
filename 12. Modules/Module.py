import time
import os
import pandas

while True: 
    if os.path.exists("Text files/temps_today.csv"):
        data = pandas.read_csv("Text files/temps_today.csv")
        print(data.mean()["st1"])

    else:
        print("File does no exist")
    time.sleep(10)



