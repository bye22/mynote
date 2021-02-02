1.进入su

jiqing@Ubuntu:~$ su
密码： 
root@Ubuntu:/home/jiqing# 

2.创建cleanCache.sh

#!/bin/bash
# 每一小时清除一次缓存
echo "开始清除缓存"
sync;sync;sync #写入硬盘，防止数据丢失
sleep 10 #延迟10秒
echo 3 > /proc/sys/vm/drop_caches
3.设置可执行

chmod +x cleanCache.sh 
4.创建定时器任务，以管理员的身份

  0 *  *   *   *     cd /home/jiqing/sh && ./cleanCache.sh
每小时执行一次。

这样你的电脑就不会越用越卡顿了。

如何查看cron日志？

需要先将这个日志开启。

进入配置文件中，

sudo vim /etc/rsyslog.d/50-default.conf 
将cron的日志注释去掉

cron.*  /var/log/cron.log #将cron前面的注释符去掉
重启rsyslog

sudo  service rsyslog  restart 
查看crontab日志

tail -f /var/log/cron.log   
日志是个好东西，方便调试，方便看清系统的真实情况。透过数据看问题。

专门监听特定的定时器

 tail -f /var/log/cron.log |grep dg
May 12 19:36:01 Ubuntu CRON[17186]: (jiqing) CMD (cd /home/wwwroot/default/dg/store/Public && /usr/bin/php cron.php Timer/clearSms)
May 12 19:37:01 Ubuntu CRON[17226]: (jiqing) CMD (cd /home/wwwroot/default/dg/store/Public && /usr/bin/php cron.php Timer/clearSms)

