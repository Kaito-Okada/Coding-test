import datetime
import random

year =2020
month =12
day =31
server_address_list =[
    '10.20.30.1/10',
    '10.20.30.2/10',
    '10.20.30.3/10',
    '11.22.33.1/10',
    '11.22.33.2/10',
]
response_list = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '-',
]

with open('test.txt', mode='w') as f:
    for h in range(0,24):
        for m in range(0,60):
            for s in range(0,60):
                dt = datetime.datetime(year, month, day, h, m, s)
                dt_str = dt.strftime('%Y%m%d%H%M%S')

                server_address = random.choice(server_address_list)
                res  = random.choice(response_list)

                l = dt_str + ',' + server_address + ',' + res +'\n'
                
                f.write(l)
