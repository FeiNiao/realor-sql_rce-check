import requests
import sys
import re

def check(url):
    check = "/RapAgent.xgi?CMD=GetRegInfo"
    urls = url + check
    try:
        reps = requests.get(url=urls,verify=False,timeout=10)
        a5 = re.findall("5.*",reps.text)
        a6 = re.findall("6.*",reps.text)
        a71 = re.findall("7.0.1.*",reps.text)
        a72 = re.findall("7.0.2.*", reps.text)
        if reps.status_code == 200 and (len(a5) != 0 or len(a6) != 0 or len(a71) != 0 or len(a72) != 0):
            print("\033[0;32;40m[+] {} 疑似存在瑞友天翼远程sql写入shell漏洞！！！\033[0m".format(i))            
        else:
            print("\033[0;31;40m[-] 该版本不存在漏洞或访问失败 url: {}\033[0m".format(i))
    except Exception as e:
        print("\033[0;31;40m[-] 访问失败 url : {}\033[0m".format(i))


file_path = sys.argv[2]
file = open(file_path,'r',encoding='UTF-8').read().split()


for i in file:
    if "http" not in i:
        i = "http://" + str(i)
    check(i)