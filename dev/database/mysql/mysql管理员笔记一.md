# 修改初始密码

## mysql5.7

在error log中 查看临时密码 ： `grep 'temporary password' /var/log/mysqld.log`

```
ALTER USER 'root'@'localhost' IDENTIFIED BY 'cogs.com';
```

授权其他机器登陆

```
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'cogs.com' WITH GRANT OPTION;

FLUSH  PRIVILEGES;
```

## mysql5.8
mysql8.0无法给用户授权或提示You are not allowed to create a user with GRANT的问题

提示意思是不能用grant创建用户，mysql8.0以前的版本可以使用grant在授权的时候隐式的创建用户，8.0以后已经不支持，所以必须先创建用户，然后再授权，命令如下：

```
mysql> CREATE USER 'root'@'%' IDENTIFIED BY 'cogs.com';

mysql> grant all privileges on *.* to 'root'@'%';
FLUSH  PRIVILEGES;

```


---

## 用户管理

### 创建用户

```sql
CREATE USER 'username'@'host' IDENTIFIED BY 'password';
```
> 说明：
username：你将创建的用户名
host：指定该用户在哪个主机上可以登陆，如果是本地用户可用localhost，如果想让该用户可以从任意远程主机登陆，可以使用通配符%
password：该用户的登陆密码，密码可以为空，如果为空则该用户可以不需要密码登陆服务器

### 授权

```sql
GRANT privileges ON databasename.tablename TO 'username'@'host' WITH GRANT OPTION;
```

>说明:
privileges：用户的操作权限，如SELECT，INSERT，UPDATE等，如果要授予所的权限则使用ALL
databasename：数据库名
tablename：表名，如果要授予该用户对所有数据库和表的相应操作权限则可用*表示，如*.*

### 撤销用户权限
```sql
REVOKE privilege ON databasename.tablename FROM 'username'@'host';
```
### 查看授权
```sql
SHOW GRANTS FOR 'pig'@'%'; 
```


### 设置与更改用户密码

```sql
SET PASSWORD FOR 'username'@'host' = PASSWORD('newpassword');
```
当前用户
```sql
SET PASSWORD = PASSWORD("newpassword");
```

### 删除用户

```sql
DROP USER 'username'@'host';
```

# Server最大接受的数据包大小

## 临时
`mysql> show VARIABLES like 'max_allowed_packet';`

`mysql> show global VARIABLES like 'max_allowed_packet';`

max_allowed_packet的单位为字节

`set global max_allowed_packet = 2*1024*1024*10;`

## 修改配置

`my.cnf`文件,在`[mysqld]`段或者mysql的server配置段
