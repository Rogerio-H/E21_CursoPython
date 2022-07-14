# e084b.py

import time 
from datetime import datetime
a = 0 
while a < 16:
    hj = datetime.now()
    hj = f'{hj.day}/{hj.month}/{hj.year} {hj.hour}:{hj.minute}:{hj.second}'
    print(hj)
    a =+ 1
    time.sleep(1)

