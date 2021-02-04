import pprint
import datetime
import sys

def open_log_txt(target_log_txt):
    with open(target_log_txt, "r", encoding="utf8")as fobj:
        server_log_dict ={}
        server_name_list=[]
        for line in fobj:
            l = [x.strip() for x in line.split(',')]

            l[0] = datetime.datetime.strptime(l[0], '%Y%m%d%H%M%S')

            tmp_dict ={
                'date':l[0],
                'response_time':l[2],
            }

            server_log_dict.setdefault(l[1], []).append(tmp_dict)
            if l[1] in server_name_list:
                pass
            else:
                server_name_list.append(l[1])

        for server_name in server_name_list:
            sorted_list = sort_datetime(server_log_dict[server_name])
            server_log_dict[server_name] = sorted_list

    return server_log_dict,server_name_list


def sort_datetime(target_list):
    sorted_list = sorted(target_list, key=lambda x: x['date'])

    return sorted_list

def calc_error_duration(s,e):
    tmp_s = s.strftime("%Y年%m月%d日%H時%M分%S秒").strip()
    tmp_e = e.strftime("%Y年%m月%d日%H時%M分%S秒").strip()
    str_error_duration = tmp_s + '~' + tmp_e

    return str_error_duration

def error_check(log_list,n):    
    error_flag = 0
    server_error_flag = 0
    cnt = 0

    error_start = 0
    error_end = 0

    error_duration_list =[]
    
    for l in log_list:
        if  error_flag == 0 and '-' in l.values():
            cnt +=1
            error_start = l['date']
            error_flag = 1
        elif error_flag ==1 and '-' in l.values():
            cnt +=1
            if cnt >= n:
                server_error_flag = 1
        elif error_flag ==1 and '-' not in l.values():
            if server_error_flag == 1:
                server_error_flag = 0
                error_end = l['date']
                error_duration_list.append(calc_error_duration(error_start,error_end))
            cnt = 0
            error_flag = 0
        else:
            pass
    
    if server_error_flag == 1:
        server_error_flag = 0
        error_end = datetime.datetime.now()
        error_duration_list.append(calc_error_duration(error_start,error_end))
         
    return error_duration_list

if __name__== "__main__":
    args = sys.argv
    target_log_txt = args[1]
    n = int(args[2])

    server_log_dict,server_name_list = open_log_txt(target_log_txt)

    for server_name in server_name_list:
        error_duration_list = error_check(server_log_dict[server_name],n)
        print('---サーバ「%s」の状況---'%server_name)
        if error_duration_list:
            print(' -故障...「発生」%d回発生しています。'%len(error_duration_list))
            for i,nd in enumerate(error_duration_list,1):
                print('   %d回目:故障期間は「%s」です。'%(i,nd))            
        else:
            print(' -故障...「なし」')
