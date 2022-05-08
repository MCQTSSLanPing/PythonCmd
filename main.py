#这是一个使用Python语言编写的命令提示符（CMD）程序，由某无聊的中学生编写
print('Mrchai’s PyCmd [版本 1.0]  Copyright Chai。保留所有权利。')     #程序介绍，没啥用
#以下为import区
import os     #导入os库
import platform     #导入platform库

#以下为命令列表,用于提示玩不明白的User
allcommand = ['test','openfile','mkdir','pycmd?','computer','dir','cd','remove','rename']

#以下为初始化区
contfolder = 0     #一个供mkdir命令调用的变量，用于防止文件夹重名
systemusername = os.getlogin()     #取系统登录用户名
dirname = os.getcwd()     #取工作目录，用于供cd命令等调用
a = os.listdir()
n = len(a)
dirname1 = ''
removefilename = ''
renamefilename = ''
contdir = 0     #初始化供dir命令调用的文件数量
dirprint = 0     #有关dir命令
openfilepath = ''     #有关open命令
print(os.name + ' user')     #打印user信息
#重复运行，防止只能输入一次命令
while True:
#以下为正式程序：
    print(dirname)     #打印工作目录
    print('在这里输入PyCmd命令：')
    a = os.listdir()     #一个必须放在while True下级语句中的初始化
    n = len(a)     #同上
    userscommand = input()     #正式程序的开始，使使用者输入想让PyCmd执行的命令
    if userscommand == 'pycmd?':  #检测User输入的命令是否存在及提示User
        print('There are all command in PyCmd')
        print(*allcommand, sep='  ')
    if userscommand == 'test':     #test命令,测试程序是否正常运行
        print('TestSuccess,welcome to use PyCmd')
        print('This is your system username:' + systemusername)
    if userscommand == 'openfile':     #一个打印文件的命令，也就是openfile
        print('请输入需要打开的文件名：')
        dirname1 = input()
        file = open(dirname1, encoding='utf-8')     #打开文件
        text = file.read()     #读文件数据
        print(text)     #输出文件中的内容（仅限txt）
    if userscommand == 'mkdir':     #在运行目录下创建一个文件夹，暂不支持更改文件夹名称
        os.mkdir('NewFolder'+str(contfolder))     #用os库中的命令创建文件夹，并防止重名
        contfolder += 1     #防止第二次创建文件夹重名情况出现
        print('success!')     #提示user创建成功
    if userscommand == 'computer':     #获取此电脑信息并打印
        print(platform.uname())
    if userscommand == 'dir':     #打印目录下所有文件名
        for i in range(n):
            print(a[dirprint] + '  ')
            dirprint += 1
    if userscommand == 'cd':     #切换文件操作路径
        print('请输入需要切换到的路径：')
        dirname = input()
        os.chdir(dirname)
    if userscommand == 'remove':     #删除文件
        print('请输入需要删除的文件名：')     #提示user输入
        removefilename = input()     #检测输入并赋值给removefilename
        os.remove(removefilename)     #利用os库删除文件
        print('success!')
    if userscommand == 'rename':     #重命名
        print('请输入需要重命名的文件名：')     #提示输入
        renamefilename = input()     #检测输入并赋值给renamefilename
        print('请输入更改完成后的文件名：')     #提示输入需要的文件名
        newname = input()     #检测输入并赋值给newname变量
        os.rename(renamefilename,newname)     #利用os库重命名文件
        print('success!')
    if userscommand == 'taskkill':     #结束任务
        print('请输入需要结束的pid:')
        pid = input()
        os.popen('taskkill.exe /pid:' + str(pid))
    if userscommand == 'tasklist':     #任务列表
        q = os.system('tasklist')
        print(q)
    if userscommand == 'size':
        print('请输入需要查询大小的文件名：')
        L = input()
        os.path.getsize(L)
    else:
        print('UnknownCommand')










