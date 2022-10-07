#功能：输出下载第三方库的命令
#作者：徐闻
#联系方式：phyxuwen@qq.com

import os

def exlink(pack_name):
    """
    输入需要下载的第三方库的名字，就可以返回下载的指令
    """
    order = 'pip install ' + pack_name + ' -i http://pypi.mirrors.ustc.edu.cn/simple/ \
--trusted-host pypi.mirrors.ustc.edu.cn --user'
    return order

def pcmd(link):
    """
    输入cmd中的下载指令，然后直接进入cmd运行指令，最后打印出cmd中的结果。
    """
    result = os.popen(link)
    context = result.read()
    for line in context.splitlines():
        print(line)
    result.close()

if __name__ == "__main__":
    print("欢迎使用，程序正在运行")
    #判断指令
    i = 'Y'
    while i in ['y', 'Y']:
        pack_name = input("请输入需要下载的第三方库的名称：")
        if pack_name == 'quit':
            break
        link = exlink(pack_name)
        print("正在下载。。。")
        pcmd(link)
        i = input("\n是否继续运行程序[y/n]:")
        #判断指令是否正确，否则重新输入
        while i not in ['y', 'Y', 'n', 'N', 'quit']:
            i = input("指令错误，请重新输入指令[y/n]:")
    print("欢迎下次使用，程序已退出")