# define _*_coding:utf-8
from globe_var import *
import paramiko
import time

def shell_cmd():
    for serv_name_key, ip_value in serv_ip.items():
        print(u'连接%s' % ip_value.encode('mbcs'))
        print(u'准备部署%s\n' % serv_name_key.encode('mbcs'))
        if serv_name_key == 'api2':
            serv_name_key = 'api'
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip_value, 22, 'root', 'root123')
        shell_name = serv_name_key+'.sh'
        cmd = './'+shell_name
        stdin,stdout,stderr=client.exec_command('cd /home/linkdsp/project/deploy/ &&'+cmd)
        print stdout.read()
        client.close()
        print(u'%s部署完毕\n' % serv_name_key.encode('mbcs'))

    print(u'全部war包已经部署，tomcat正在重启，请稍后刷新'.encode('mbcs'))



        # shell_name = serv_name_key+'.sh'
        # cmd = './'+shell_name
        #
        # t = paramiko.Transport((ip_value, 22))
        # t.connect(username='root', password='root123')
        # chan = t.open_session()
        # chan.get_pty()
        # chan.invoke_shell()
        # time.sleep(10)
        # chan.send('cd /home/linkdsp/project/deploy/ &&'+cmd)
        # time.sleep(30)
        # print chan.recv(65535)
        # t.close()
        # print('%s部署完毕' % serv_name_key)



