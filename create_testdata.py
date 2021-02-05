import datetime

year =2020
month =12
day =31

with open('testdata_for_max.txt', mode='w') as f:
    for h in range(0,24):
        for m in range(0,60):
            for s in range(0,60):
                dt = datetime.datetime(year, month, day, h, m, s)
                dt_str = dt.strftime('%Y%m%d%H%M%S')
                l = dt_str + ',10.20.30.1/16,2\n'
                
                f.write(l)
