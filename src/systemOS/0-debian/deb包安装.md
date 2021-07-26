# deb包安装

## sudo dpkg -i  xxxx

## 连同配置文件一起删除 dpkg -r --purge xxx.deb

## 删除软件包 dpkg -r xxx.deb

## 查看软件包信息 dpkg -info xxx.deb

## dpkg -l |grep ^rc|awk '{print $2}' |sudo xargs dpkg -P



