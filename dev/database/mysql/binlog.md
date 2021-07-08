# Mysql - binlog

**开启**

1. 停止服务

```
 # service mysqld stop
```

2. 配置

```
server-id=1
log-bin=mysql-bin
    OR
log-bin = /var/lib/mysql/<application-name>-mysql-bin.log
expire_logs_days = 2
binlog_format=mixed # Recommended binary logging format – mixed
```

3. 启动服务

4. 问题
mysqlbinlog: [ERROR] unknown variable 'default-character-set=utf8'

**方案**
一是在MySQL的配置/etc/my.cnf中将default-character-set=utf8 修改为 `character-set-server = utf8`
二是用`mysqlbinlog --no-defaults mysql-bin.000004`
