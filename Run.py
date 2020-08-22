import Network
import Loginfo
import json
import shutil
import os
import threading
import DataAnalyze
import random
import sys
import urllib.request
MAX_THREADS = 4
def analyze():
    files = os.listdir('Catch')
    lock = threading.Lock()
    for f in files:
        while len(DataAnalyze.threadpool)>=MAX_THREADS:
            pass
        id = random.randint(1,152522155)
        while id in DataAnalyze.threadpool:id = random.randint(1,152522155)
        #防止线程id重复
        thr = DataAnalyze.Analyze(lock,open('Catch/'+f,'r',encoding='utf-8'),id,f)
        DataAnalyze.threadpool[id] = thr
        thr.start()
    while len(DataAnalyze.threadpool):pass
    visitors = Loginfo.tempTable.values()
    for i in visitors:
        Loginfo.sheet.append(i)
    Loginfo.sheet.writeToExcel()
last = False
cloudcookie = False
if len(sys.argv)>1:
    for arg in sys.argv:
        if arg == '-last' or arg == 'last':
            last = True
        if arg == 'debug' or arg == '-debug':
            cloudcookie = True

if last:
    print("开始分析上一次结果")
    analyze()
    print("分析完成")
    exit()


usr = sys.argv[1]
uin = sys.argv[2]
Loginfo.info.usr = usr
Loginfo.info.host = uin
if cloudcookie:#从github上获取cookie
    #主要是为了方便部署到香橙片
    try:
        conn = urllib.request.urlopen("https://denghaoyu.github.io/cookie.html")
        Loginfo.info.cookie = json.loads(str(conn.read()))
    except Exception as e:
        print("Exception has occurred when getting cookies from github:",e)
        exit()
else:
    try:
        f = open('cookie.txt', "r")
        Loginfo.info.cookie = json.load(f)
    except FileNotFoundError:
        print("Ooooooooooooooops,cookie.txt 文件丢失，请检查")
        exit()

if not Network.checkCookieAndRight(uin):
   print("Oooooooooooooooops,权限错误，请检查是否有权访问对方空间或者cookie错误")
   exit()

limit = int(sys.argv[3])
cnt = 0
if os.path.exists("Catch"):
    if os.listdir("Catch"):
        print("Catch文件夹不为空，是否清除（Y/N），如只需统计上一次爬取结果，在运行时加入参数-last")
        op = input()
        if op == 'Y':
            shutil.rmtree('Catch')
            os.mkdir('Catch')
        else:
            exit()
else:
    os.mkdir("Catch")
while limit>0:
    try:
        Network.spideToCatch(cnt + 1,min(limit, 20))
        cnt += min(limit, 20) - 1
        limit -= min(limit, 20)
        if limit==0:break
        else : limit+=1
    except Exception as e:
        print("Ooooops,爬取说说时发生了错误:",e)
        exit()
print("开始解析")
analyze()

print("爬完啦，祝您撩汉成功,爬取了%d条说说"%cnt)
