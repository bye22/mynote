# centos7时间同步和时区设置

-  安装ntp服务的软件包
sudo yum install ntp

- 将ntp服务设置为缺省启动
systemctl enable ntpd

- 修改启动参数，增加-g -x参数，允许ntp服务在系统时间误差较大时也能正常工作
sudo vi /etc/sysconfig/ntpd

- 启动ntp服务
sudo service ntpd restart

- 将系统时区改为上海时间 (亦即CST时区)
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

- 查看时间是否正确
执行date命令即可。