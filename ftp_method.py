# _*_coding:utf-8 _*_
# from ftplib import FTP
import os
from globe_var import *
import paramiko

def ftp_method(dirs):
    # #遍历dict，连接服务器，上传war包
    # for serv_name_key, ip_value in serv_ip.items():
    #     print('serv_name:%s' % serv_name_key)
    #     print('serv_ip:%s' % ip_value)
    #     print('正在上传%s包' % serv_name_key)
    #     ftp = FTP()
    #     ftp.set_debuglevel(2)
    #     ftp.connect(ip_value, 21)
    #     ftp.login('root', 'root123')
    #     bufsize = 1024
    #     war_name = serv_name_key+'.war'
    #     file_name = os.path.join(dirs, war_name)
    #     print('filename:%s' % file_name)
    #     ftp.cwd('/home/linkdsp/project')
    #     file_handle = open(file_name, 'rb')
    #     ftp.storbinary('STOR%s'%os.path.basename(file_name), file_handle, bufsize)
    #     ftp.set_debuglevel(0)
    #     file_handle.closed
    #     ftp.quit()
    #     print('%s包上传完毕' % serv_name_key)
    for serv_name_key, ip_value in serv_ip.items():
        print('serv_ip:%s' % ip_value)
        print(u'正在上传%s包' % serv_name_key.encode('mbcs'))
        if serv_name_key == 'api2':
            serv_name_key = 'api'

        t = paramiko.Transport((ip_value, 22))
        t.connect(username='root', password='root123')
        sftp = paramiko.SFTPClient.from_transport(t)
        war_name = serv_name_key+'.war'
        # local_dir = os.path.join(dirs, war_name)
        remote_dir = '/home/linkdsp/project/'
        sftp.put(os.path.join(dirs, war_name), os.path.join(remote_dir, war_name))
        t.close()
        print(u'%s包已经上传完成' % serv_name_key.encode('mbcs'))

    print(u'包已全部上传服务器\n'.encode('mbcs'))

