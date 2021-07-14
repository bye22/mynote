## 错误2002(HY000)：无法通过Socket‘/var/run/mysqld/mysqld.sock’连接到本地MySQL服务器(2)



1. 检查文件是否`/var/run/mysqld/mysqld.sock`存在。

2. 如果没有，则通过以下方式手动创建`touch /var/run/mysqld/mysqld.sock`。

3. 通过输入更改所述文件的所有权`chown mysql /var/run/mysqld/mysqld.sock`

4. 重新启动MySQL服务`service mysql restart`或`/etc/init.d/mysql restart`

