from datetime import datetime as dt
from time import time 

def data_log(data): 
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}\n'.format(time, data))