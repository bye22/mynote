列出已经安装的软件包

    pacman -Q

查看virtualbox包是否已经安装

    pacman -Q virtualbox

查看已安装的包virtualbox的详细信息

    pacman -Qi virtualbox

列出已安装包virtualbox的所有文件

    pacman -Ql virtualbox

查找某个文件属于哪个包

    pacman -Qo /etc/passwd

查询包组

    pacman -Sg

查询包组所包含的软件包

    pacman -Sg gnome

搜索virtualbox相关的包

    pacman -Ss virtualbox

从数据库中搜索virtualbox的信息

    pacman -Si virtualbox
---

仅同步源

    sudo pacman -Sy

更新系统

    sudo pacman -Su

同步源并更新系统

    sudo pacman -Syu
---

同步源后安装包

    sudo pacman -Sy virtualbox

安装包组

     pacman -S xfce4

```
有的包组包含大量的软件包，有时用户只需其中几个。除了逐一键入序号外，pacman 还支持选择或排除某个区间内的的软件包：

Enter a selection (default=all): 1-10 15
这将选中序号 1 至 10 和 15 的软件包。而

Enter a selection (default=all): ^5-8 ^2
将会选中除了序号 5 至 8 和 2 之外的所有软件包。

```

从本地数据库中获取virtualbox的信息，并下载安装

    sudo pacman -S virtualbox

强制安装virtualbox包

    sudo pacman -Sf virtualbox
---

删除virtualbox

    sudo pacman -R virtualbox

强制删除被依赖的包（慎用）

    sudo pacman -Rd virtualbox

删除virtualbox包及依赖其的包

    sudo pacman -Rc virtualbox

删除virtualbox包及其依赖的包

    sudo pacman -Rsc virtualbox
---

清理/var/cache/pacman/pkg目录下的旧包

    sudo pacman -Sc

清除所有下载的包和数据库

    sudo pacman -Scc

---

安装下载的virtualbox包（有时候需要降级包的时候就用这个）

    cd /var/cache/pacman/pkg
    sudo pacman -U virtualbox-5.2.12-1-x86_64.pkg.tar.xz

升级时不升级virtualbox包

    sudo pacman -Su --ignore virtualbox

---

- TODO 
  1. 区分操作类别 : 查询，安装，卸载，升级，降级
  2. 在（1）的基础上，区分命令安全级别
