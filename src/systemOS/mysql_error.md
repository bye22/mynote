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