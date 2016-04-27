# _*_ coding:utf-8 _*_
from rm_war import *
from compile_war import *
from ftp_method import *
from globe_var import *
from shell_cmd import *


# 输入源代码在本机上的路径
code_address = raw_input(u"输入源代码在本机上的路径:".encode('mbcs'))
split_name = code_address.split('\\')
drive_name = split_name[0]
copy_dirs = os.path.join(drive_name, '/war')
# 删除原有war包
rm_war(drive_name, code_address, copy_dirs)
#编译代码成war包
result = compile_war(drive_name, code_address, copy_dirs)
if result == True:
    #通过sftp方式，把war包上传到服务器
    ftp_method(copy_dirs)
    #远程访问服务器，执行shell脚本
    shell_cmd()
