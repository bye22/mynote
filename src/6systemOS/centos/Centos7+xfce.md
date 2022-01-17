# 更新
$ yum update

# 查看是否有xfce组：
$ yum grouplist

# 额外源
$ yum install epel-release -y

yum groupinstall "X Window system"

$ yum groupinstall xfce

# 启动

$ systemctl isolate graphical.target


# 安装楷体字体
$ yum install cjkuni-ukai-fonts