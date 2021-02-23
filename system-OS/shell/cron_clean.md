http://c.biancheng.net/view/1092.html

[root@localhost ~]# service crond restart
停止 crond： [确定]
正在启动 crond： [确定]
#重新启动crond服务
[root@localhost ~]# chkconfig crond on
#设定crond服务为开机自启动


表 1 crontab 命令常用选项及功能
选项	功能
-u user	用来设定某个用户的 crontab 服务，例如 "-u demo" 表示设备 demo
用户的 crontab 服务，此选项一般有 root 用户来运行。
-e	编辑某个用户的 crontab 文件内容。如果不指定用户，则表示编辑当前用户的 crontab 文件。
-l	显示某用户的 crontab 文件内容，如果不指定用户，则表示显示当前用户的 crontab 文件内容。
-r 	从 /var/spool/cron 删除某用户的 crontab 文件，如果不指定用户，则默认删除当前用户的 crontab 文件。 
-i	在删除用户的 crontab 文件时，给确认提示。


[root@localhost ！]# crontab -e
#进入 crontab 编辑界面。会打开Vim编辑你的任务
* * * * * 执行的任务

表 2 crontab 时间表示
项目	含义	范围
第一个"*"	一小时当中的第几分钟（minute）	0~59
第二个"*"	一天当中的第几小时（hour）	0~23
第三个"*"	一个月当中的第几天（day）	1~31
第四个"*"	一年当中的第几个月（month）	1~12
第五个"*"	一周当中的星期几（week）	0~7（0和7都代表星期日）


表 3 时间特殊符号
特殊符号	含义
*（星号）	代表任何时间。比如第一个"*"就代表一小时种每分钟都执行一次的意思。
,（逗号）	代表不连续的时间。比如"0 8，12，16***命令"就代表在每天的 8 点 0 分、12 点 0 分、16 点 0 分都执行一次命令。
-（中杠）	代表连续的时间范围。比如"0 5 ** 1-6命令"，代表在周一到周六的凌晨 5 点 0 分执行命令。
/（正斜线）	代表每隔多久执行一次。比如"*/10****命令"，代表每隔 10 分钟就执行一次命令。

表 4 crontab举例
时间	含义
45 22 ***命令	在 22 点 45 分执行命令
0 17 ** 1命令	在每周一的 17 点 0 分执行命令
0 5 1，15**命令	在每月 1 日和 15 日的凌晨 5 点 0 分执行命令
40 4 ** 1-5命令	在每周一到周五的凌晨 4 点 40 分执行命令
*/10 4 ***命令	在每天的凌晨 4 点，每隔 10 分钟执行一次命令
0 0 1，15 * 1命令	在每月 1 日和 15 日，每周一个 0 点 0 分都会执行命令，注意：星期几和几日最好不要同时出现，因为它们定义的都是天，非常容易让管理员混淆


---

1.进入su
```bash
jiqing@Ubuntu:~$ su
密码： 
```
2.创建cleanCache.sh
```bash
#!/bin/bash
# 每一小时清除一次缓存
echo "开始清除缓存"
sync;sync;sync #写入硬盘，防止数据丢失
sleep 10 #延迟10秒
echo 3 > /proc/sys/vm/drop_caches
```
3.设置可执行
```bash
chmod +x cleanCache.sh 
```
4.创建定时器任务，以管理员的身份
```bash
  0 *  *   *   *     cd /home/jiqing/sh && ./cleanCache.sh
```
每小时执行一次。

这样你的电脑就不会越用越卡顿了。

如何查看cron日志？

需要先将这个日志开启。

进入配置文件中，
```bash
sudo vim /etc/rsyslog.d/50-default.conf 
将cron的日志注释去掉

cron.*  /var/log/cron.log #将cron前面的注释符去掉
重启rsyslog
```
```bash
sudo  service rsyslog  restart 
查看crontab日志
```
```bash
tail -f /var/log/cron.log   
日志是个好东西，方便调试，方便看清系统的真实情况。透过数据看问题。
```
专门监听特定的定时器

```bash
tail -f /var/log/cron.log |grep dg

May 12 19:36:01 Ubuntu CRON[17186]: (jiqing) CMD (cd /home/wwwroot/default/dg/store/Public && /usr/bin/php cron.php Timer/clearSms)
May 12 19:37:01 Ubuntu CRON[17226]: (jiqing) CMD (cd /home/wwwroot/default/dg/store/Public && /usr/bin/php cron.php Timer/clearSms)
```
