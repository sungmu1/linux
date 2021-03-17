#!/bin/python3
#부하테스트용

import os
import subprocess
import time

root_path = '/'
here_path = os.getcwd()

test_factor = [
        '1. app_test',
        '2. disk_io'
        ]#추가 바람

def timer():
    start_time = time.time()
    return start_time

def test():
    return os.system('ps -ef | grep gnome | awk \'{print $2}\' ')

def CreateFolder(directory):
    try:
        if not os.path.isdir(directory):
            os.makedirs(directory)
    except OSError:
        print('이미 존재하는 폴더임' + directory)

def DeleteFolder(directory):
    try:
        if os.path.isdir(directory):
            os.rmdir(directory)
    except OSError:
        print('지울 폴더가 없음' + directory)

def diskIO():
    dir_name = 'diskIO_test_directory'
    directory = os.path.join(here_path, dir_name)
    
    CreateFolder(directory)
    time.sleep(10)
    DeleteFolder(directory)

def AppTest(appName):
    proc=subprocess.Popen(appName)
    time.sleep(10)
    proc.terminate()
    while False :
    #while proc.poll() is None:
        print('wait')
        proc.Popen.terminate()
        time.sleep(2)


def main() :
    start_time = timer()
    DISPLAY = "localhost:10.0" 
#    killApp = 'pkill -9 -ef togate'
    for display in test_factor :
       print(display)
    print ('num select >>', end= ' ')
    test_case = input()

    if test_case == '1' : #App Test
        appCount = 0
        print('app name >>', end = ' ')
        appName = input()
        while True :
            AppTest(appName)
            #os.system(killApp)
            appCount=appCount+1
            if time.time() - start_time > 3600: #time over (1 hour)
                break
        print('test app : {}'.format(appName))
        print('app count : {}'.format(appCount))

    elif test_case == '2' : #directory IO Test
        while True :
            diskIO()
            if time.time() - start_time > 60 : #time over (1 hour)
                break
    else :
        print('잘못 입력함')


    return 0



if __name__ == "__main__":
    main()

#os.system(killApp)
