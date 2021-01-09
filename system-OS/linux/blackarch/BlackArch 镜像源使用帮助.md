# BlackArch 镜像源使用帮助

仓库地址：blackarch.org/blackarch/

/etc/pacman.conf 文件末尾添加两行：

```
[blackarch]
SigLevel = Optional TrustAll
Server = https://mirrors.ustc.edu.cn/blackarch/$repo/os/$arch
```


收录的工具列表： http://blackarch.org/tools.html