# -*-coding: utf-8 -*-
import inspect
from datetime import datetime
import os
import os.path

def save_log(contents, subject="None", folder=""):
    current_dir = os.getcwd()
    filePath = current_dir + os.sep + folder + os.sep + cur_month() + ".txt"
    openMode = ""
    if (os.path.isfile(filePath)):
        openMode = 'a'
    else:
        openMode = 'w'
    line = '[{0:<8}][{1:<10}] {2}\n'.format(cur_date_time(), subject, contents)

    with open(filePath, openMode, encoding='utf8') as f:
        f.write(line)
    pass

def whoami():
    return '* ' + cur_time_msec() + ' ' + inspect.stack()[1][3] + ' '
    
def whosdaddy():
    return '*' + cur_time_msec() + ' ' + inspect.stack()[2][3] + ' '
    
def cur_date_time():
    cur_time = datetime.now().strftime('%y-%m-%d %H:%M:%S')
    return cur_time

def cur_time_msec():
    cur_time = datetime.now().strftime('%H:%M:%S.%f') 
    return cur_time

def cur_date():
    cur_time = datetime.now().strftime('%y-%m-%d')
    return cur_time

def cur_month():
    cur_time = datetime.now().strftime('%y-%m')
    return cur_time

def cur_time():
    cur_time = datetime.now().strftime('%H:%M:%S')
    return cur_time

if __name__ == "__main__":
    print(cur_time())
    print(cur_date())
    print(cur_date_time() )
    save_log("한글", "한글", "log")