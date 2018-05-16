2018/02/06
ssh-keygen -t rsa -b 4096 -C "freeordie@126.com"
一行最好不要超过79个字符

2018/02/07
Anaconda3

2018/02/08
1.编辑/etc/udev/rules.d/70-persistent-net.rules,
找到与ifconfig -a得出的MAC相同的一行（NAME='eth1'这一行），
把它改为"NAME=eth0 "，然后把上面一行（NAME='eth0'）删除掉。


>>> sys.path
>>>

生成pyc文件
python -m compileall test_psutil.py

2018/02/10
support@nord-cn.net

conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
