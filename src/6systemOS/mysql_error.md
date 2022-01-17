mysql5.7 误删管理员root%'localhost'账户

1. 
--skip-grant-tables

2. 重启服务

3. 

```
use mysql;
insert into user set user='root',ssl_cipher='',x509_issuer='',x509_subject='';
flush privileges;

GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' IDENTIFIED BY 'mN6WT8c#' WITH GRANT OPTION; 
flush privileges;
```

4. #--skip-grant-tables 重启服务


5. Column count of mysql.user is wrong. Expected 45, found 43

```
mysql_upgrade -s -p
```

6. Access denied for user 'root'@'%' (using password: YES)
> 权限问题

GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '123.com' WITH GRANT OPTION; 

flush privileges;

7. The user specified as a definer ('wushuo'@'%') does not exist

1. 重新创建试图

2. 
 复制视图创建语句，直接将create改成alter，definer改成相关的，比如root@localhost  例如：
用alter view 修改definer的值，alter ALGORITHM=UNDEFINED DEFINER=`public`@`192.168.0.%` SQL SECURITY DEFINER VIEW `view_product` AS 视图选择语句。

通过执行use information_schema;和 select TABLE_SCHEMA,TABLE_NAME,DEFINER from views; 两条语句，可以查询到definer是否更改成功了。