# Mysql 导入文件提示 --secure-file-priv option 问题


MYSQL导入CSV格式文件数据执行提示错误（ERROR 1290）：

The MySQL server is running with the --secure-file-priv option so it cannot execute this statement.

# 解析
目录权限问题。
SHOW VARIABLES LIKE "secure_file_priv";

（1）NULL，表示禁止。

（2）如果value值有文件夹目录，则表示只允许该目录下文件（PS：测试子目录也不行）。

（3）如果为空，则表示不限制目录。

# 方案

## （1）方案一：

把导入文件放入secure-file-priv目前的value值对应路径即可。

##　（2）方案二：

把secure-file-priv的value值修改为准备导入文件的放置路径。

##　（3）方案三：修改配置

去掉导入的目录限制。可修改mysql配置文件（Windows下为my.ini, Linux下的my.cnf），在[mysqld]下面，查看是否有：

secure_file_priv =

如上这样一行内容，如果没有，则手动添加。如果存在如下行：

secure_file_priv = /home 

这样一行内容，表示限制为/home文件夹。而如下行：

secure_file_priv =

这样一行内容，表示不限制目录，等号一定要有，否则mysql无法启动。

修改完配置文件后，重启mysql生效。