import os

def banner():
    print('+-----------------------------------------------+')
    print('+ \033[1;36mwxscan-1.0              \033[0m\t\t\t+')
    print('+ \033[1;36m作者:r00t&jiangwhale     \033[0m\t\t\t+')
    print('+ \033[1;36m使用帮助如下              \033[0m\t\t\t+')
    print('+ \033[1;36m1、调用masscan扫描ip      \033[0m\t\t\t+')
    print('+ \033[1;36m2、处理masscan扫描之后的ip \033[0m\t\t\t+')
    print('+ \033[1;36m3、标题状态码识别          \033[0m\t\t\t+')
    print('+ \033[1;36m4、指纹识别               \033[0m\t\t\t+')
    print('+ \033[1;36m5、扫描漏洞               \033[0m\t\t\t+')
    print('+-----------------------------------------------+')

def masscan_find():
    f = open('result.txt', 'r+')
    for i in f.readlines():
        str = i.strip()


        a = str.find("port")
        b = str.find("/")
        c = str.find("on")

        m = str[a+5:b]

        n = str[c+3:]

        url = "http://" +n +":"+ m

        w = open("url.txt", "a")
        w.write(url + '\r\n')

if __name__ == '__main__':
    banner()
    a = int(input("请输入你要选择的操作:"))
    if a == 1:
        ip = input("请输入要扫描的ip(192.168.1.1|192.168.1.1/24):")
        ml_1 = './masscan ' + ip + ' -p1-65535 --rate=10000 > result.txt'
        os.system(ml_1)
    elif a == 2:
        masscan_find()
    elif a == 3:
        ml_2 = 'cat url.txt |./httpx -title -content-length -status-code -mc 200,302 -silent'
        os.system(ml_2)
    elif a == 4:
        ml_3 = './main finger -l url.txt '
        os.system(ml_3)
    elif a == 5:
        ml_4 = './afrog -T url.txt -o result.html'
        os.system(ml_4)