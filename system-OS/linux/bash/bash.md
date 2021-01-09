  解决 sudo echo x > 时的 Permission denied错误

运行下面语句清缓存时，报Permission denied错误：-bash: /proc/sys/vm/drop_caches: Permission denied

sudo echo 1 > /proc/sys/vm/drop_caches

sudo echo 2 > /proc/sys/vm/drop_caches

sudo echo 3 > /proc/sys/vm/drop_caches

sync


bash 拒绝这么做，提示权限不够，是因为重定向符号 “>” 也是 bash 的命令。sudo 只是让 echo 命令具有了 root 权限，
但是没有让 “>” 命令也具有root 权限，所以 bash 会认为这个命令没有写入信息的权限。


解决方法：

"sh -c" 命令,它可以让 bash 将一个字串作为完整的命令来执行

sudo sh -c "echo 1 > /proc/sys/vm/drop_caches"

sudo sh -c "echo 2 > /proc/sys/vm/drop_caches"

sudo sh -c "echo 3 > /proc/sys/vm/drop_caches"

或者
echo 1 |sudo tee /proc/sys/vm/drop_caches 
