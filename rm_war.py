# _*_ coding:utf-8 _*_
import os
import os.path
import glob
from globe_var import *
import shutil


'''
删除代码文件夹里的war包
删除copy出来的war文件夹里的war包

'''
def rm_war(drive_name, address, copy_dirs):
    # 循环拼接处war包路径，使用通配符进行删除代码target文件夹里的war包
    for i in range(len(last_address)):
        full_address = os.path.join(address, last_address[i])
        war_path = glob.glob(os.path.join(full_address, '*.war'))
        for path in war_path:
            os.remove(path)

    #如果在根目录存在war目录，则删除整个文件夹
    copy_war_path = copy_dirs
    if os.path.exists(copy_war_path):
        shutil.rmtree(copy_war_path)
    else:
        print(u'根目录不存在war文件夹'.encode('mbcs'))
    print(u"所有war包已删除".encode('mbcs'))
    return 0
