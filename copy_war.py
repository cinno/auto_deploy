# _*_ coding:utf-8 _*_
import os
import os.path
import glob
import shutil
from globe_var import *
'''
在根目录新建war文件夹
将taget文件里的包复制到war文件夹里
'''

def copy_war(drive_name, address, copy_dirs):
    print('copying')
    dirs = copy_dirs
    if os.path.exists(dirs):
        print(u'文件夹已存在，不需要新建'.encode('mbcs'))
    else:
        os.makedirs(dirs)

    for i in range(len(last_address)):
        full_address = os.path.join(address, last_address[i])
        war_path = glob.glob(os.path.join(full_address, '*.war'))
        for path in war_path:
            shutil.copy(path, dirs)

    return True
