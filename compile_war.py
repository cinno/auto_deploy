# _*_coding:utf-8 _*_
import os
import commands
from copy_war import *

'''
对源代码路径进行分隔，取出盘符
调用cmd命令，依次对源代码进行编译，编译成war包
判断war包存在后 将war包cpoy到根目录下的war文件夹里
'''
def compile_war(drive_name, address, copy_dirs):
    #调用cmd命令，进行编译
    cmd = '%s && cd %s && mvn -Dmaven.test.skip=true clean install -Pall'%(drive_name, address)
    print(cmd)
    cmd_result = os.system(cmd)
    # 如果编译失败，则输出控制台内容
    if cmd_result != 0:
        print(u"编译失败".encode('mbcs'))
        return False
    # 如果编译成功，则把war包拷贝走，进行cron的编译
    if cmd_result == 0:
        copy_war(drive_name, address, copy_dirs)
        cmd2 = '%s && cd %s && mvn -Dmaven.test.skip=true clean install -Pcron'%(drive_name, address)
        # (status, output) = commands.getstatusoutput(cmd2)
        cmd_result = os.system(cmd2)
        if cmd_result != 0:
            # print(output.decode('gbk').encode('utf-8'))
            print(u"编译失败".encode('mbcs'))
            return False
        else:
            copy_war(drive_name, address, copy_dirs)
            #判断是否所有包都已复制过去
            # dirs = os.path.join(drive_name, 'war')
            # if os.path.exists()
            print(u'所有包都已编译成功，并拷贝到根目录下的war文件夹\n'.encode('mbcs'))
            return True

