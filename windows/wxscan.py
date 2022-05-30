import os
import re
from time import time

def banner():
    print('+-----------------------------------------------+')
    print('+ \033[1;36mwxscan-2.0              \033[0m\t\t\t+')
    print('+ \033[1;36m作者:r00t&jiangwhale     \033[0m\t\t\t+')
    print('+ \033[1;36m使用帮助如下              \033[0m\t\t\t+')
    print('+ \033[1;36m1、kscan扫描             \033[0m\t\t\t+')
    print('+ \033[1;36m2、处理kscan扫描之后的ip \033[0m\t\t\t+')
    print('+ \033[1;36m3、指纹识别               \033[0m\t\t\t+')
    print('+ \033[1;36m4、扫描漏洞               \033[0m\t\t\t+')
    print('+ \033[1;36m5、hydra自动化爆破         \033[0m\t\t\t+')
    print('+-----------------------------------------------+')

def masscan_find():
    f = open('result.txt', 'r+')
    w = open("url.txt", "w")
    w.write('')
    sum = 0
    for i in f.readlines():
        str1 = i.strip()

        if (re.findall(r"(http://)|(https://)", str1)):
            a = str1.find("\t")

            url = str1[:a]

            w = open("url.txt", "a+")
            w.write(url + '\r\n')
            w.close()
            sum += 1
    print("一共处理了"+str(sum)+"条数据")

if __name__ == '__main__':
    banner()
    a = int(input("请输入你要选择的操作:"))
    if a == 1:
        ip = input("请输入要扫描的ip(IP地址：114.114.114.114\nIP地址段：114.114.114.114/24,不建议子网掩码小于12\nIP地址段：114.114.114.114-115.115.115.115\nURL地址：https://www.baidu.com\n文件地址：file:/tmp/target.txt):")
        os.system('rm -rf result.txt')
        ml_1 = 'kscan.exe -t ' + ip + ' --top 1000 --threads 2048  -o result.txt'
        os.system(ml_1)
    elif a == 2:
        masscan_find()
    elif a == 3:
        ml_2 = 'main.exe finger -l url.txt '
        os.system(ml_2)
    elif a == 4:
        ml_3 = 'afrog.exe -T url.txt -o result.html'
        os.system(ml_3)
    elif a == 5:
        ip = input("请输入要扫描的ip(IP地址：114.114.114.114\nIP地址段：114.114.114.114/24,不建议子网掩码小于12\nIP地址段：114.114.114.114-115.115.115.115\nURL地址：https://www.baidu.com\n文件地址：file:/tmp/target.txt):")
        ml_4 = 'kscan.exe -t ' + ip + ' --hydra --threads 2048'
        os.system(ml_4)