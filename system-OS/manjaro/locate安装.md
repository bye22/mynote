# locate 命令
- https://commandnotfound.cn/linux/1/315/locate-%E5%91%BD%E4%BB%A4

## locate 命令安装：

```bash
-bash: locate: command not found
 
#Debian
apt-get install mlocate
 
#Ubuntu
apt-get install mlocate
sudo updatedb #更新库
 
#Alpine
apk add mlocate
 
#Arch Linux
pacman -S mlocate
 
#Kali Linux
apt-get install mlocate
 
#CentOS
yum install mlocate
 
#安装完再尝试用locate定位内容，发现依然不好使，报了新的错误: 
#locate: can not stat () `/var/lib/mlocate/mlocate.db': No such file or directory
#原因是安装完后没有更新库，执行下面命令更新库：
ubdatedb 
 
#Fedora
dnf install mlocate
 
#Raspbian
apt-get install mlocate
 
#Docker
docker run cmd.cat/locate locate
```

### 问题一：
---
locate: 无法执行 stat () `/var/lib/mlocate/mlocate.db': 没有那个文件或目录
--- 

root用户执行（有点慢耐心等待。。。）
```bash
updatedb
```
## locate 命令选项：

```
-e 将排除在寻找的范围之外。
-1 如果 是 1．则启动安全模式。在安全模式下，使用者不会看到权限无法看到 的档案。这会始速度减慢，因为 locate 必须至实际的档案系统中取得档案的  权限资料。
-f 将特定的档案系统排除在外，例如我们没有到理要把 proc 档案系统中的档案  放在资料库中。
-q 安静模式，不会显示任何错误讯息。
-n 至多显示 n个输出。
-r 使用正规运算式 做寻找的条件。
-o 指定资料库存的名称。
-d 指定资料库的路径
-h 显示辅助讯息
-V 显示程式的版本讯息
```

## locate 命令文件位置：
```
/var/lib/mlocate/mlocate.db
```

## locate 命令实例
查找和 php-fpm 相关的所有文件：
```
locate php-fpm

```

用 locate 搜索 etc 目录下，所有以 m 开头的文件：
```
locate /etc/m
```