#coding=gbk

import os
import os.path

os.system("cls")
print ("adb ������...")
os.popen("adb devices")
os.system("cls")

rt = os.popen('adb devices').readlines()#os.popen()ִ��ϵͳ�������ִ�к����Ϣ����
n = len(rt) - 2
print (rt)
print ("��⵽" + str(n) + "̨�豸��")
ds = list(range(n))
for i in range(n):
	nPos = rt[i+1].index("\t")

	ds[i] = rt[i+1][:nPos]
	print (str(i+1) + " - " + ds[i])
print (" ")
nSel = 1
if n != 1:
	nSel = int(input("ѡ���豸��"))
if nSel <= n:
	dev = ds[nSel-1]

fn = input("�����ļ�����")
fd = open(fn + '.cmd', 'w')

if not os.path.isdir("D:\\" + fn):
	os.mkdir("D:\\" + fn)

fd.write(":loop\n")
fd.write("adb -s ")      #ѡ���豸
fd.write(dev)            #�豸��
fd.write(" shell monkey  -p honc.td --monitor-native-crashes  --pct-touch 93 --pct-motion 7 --pct-nav 0 -s %random% -vv  --throttle 500 320000 >D:\\")#-s %random%����˼�Ƿ�ֹ��Ʒ��ͬ��ʱ������ظ�ִ��ͬһ�ֶ���
fd.write(fn)
fd.write("\\%random%.log\n")
fd.write("@ping -n 15 127.1 >nul\n")   #ping�Լ�15�������ӳ�
fd.write("adb -s ")
fd.write(dev)
fd.write(" reboot\n")
fd.write("@ping -n 120 127.1 >nul\n")
fd.write("@goto loop")

fd.close()

print ("�������������")