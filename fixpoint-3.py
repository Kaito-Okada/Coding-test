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

def error_check(log_list,n,m,t):    
    error_flag = 0
    server_error_flag = 0
    cnt = 0

    error_start = 0
    error_end = 0

    error_duration_list =[]

    server_load_flag = 0
    server_load_start = 0
    server_load_end = 0
    server_load_list = []   
    
    for i,l in enumerate(log_list,1):
        if i >= m:
            b2_rt = log_list[i-3]['response_time']
            b1_rt = log_list[i-2]['response_time']
            now_rt = l['response_time']
            
            b1_time = log_list[i-2]['date']
            now_time = l['date']

            if b2_rt != '-' and b1_rt != '-' and now_rt != '-':
                ave_rt = (float(b2_rt)+float(b1_rt)+float(now_rt))/m
                if  server_load_flag == 0 and ave_rt > t :
                    server_load_flag = 1
                    server_load_start = now_time
                elif server_load_flag == 0 and ave_rt <= t:
                    pass
                elif server_load_flag == 1 and ave_rt > t:
                    pass
                else:   
                    server_load_end = b1_time             
                    server_load_list.append(calc_error_duration(server_load_start,server_load_end))
                    server_load_flag = 0
            elif server_load_flag == 0:
                server_load_flag = 1
                server_load_start = l['date']
            else:
                pass     

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

    if server_load_flag ==1:
        server_load_end = datetime.datetime.now()
        server_load_list.append(calc_error_duration(server_load_start,server_load_end)) 

         
    return error_duration_list,server_load_list

if __name__== "__main__":
    args = sys.argv
    target_log_txt = args[1]
    n = int(args[2])
    m = float(args[3])
    t = float(args[4])

    server_log_dict,server_name_list = open_log_txt(target_log_txt)

    for server_name in server_name_list:
        error_duration_list,server_load_list = error_check(server_log_dict[server_name],n,m,t)
        print('---サーバ「%s」の状況---'%server_name)
        if error_duration_list:
            print(' -故障...「発生」%d回発生しています。'%len(error_duration_list))
            for i,nd in enumerate(error_duration_list,1):
                print('   %d回目:故障期間は「%s」です。'%(i,nd))            
        else:
            print(' -故障...「なし」')
        if server_load_list:
            print(' -過負荷状態...「発生」%d回発生しています。'%len(server_load_list))
            for i,nd in enumerate(server_load_list,1):
                print('   %d回目:過負荷状態期間は「%s」です。'%(i,nd))            
        else:
            print(' -過負荷状態...「なし」')
