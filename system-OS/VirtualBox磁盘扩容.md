1. 对虚拟磁盘文件扩容, 建议不要用图像界面, 否则很慢.

```
VBoxManage modifyhd "[Path]:\YourVisualDiskName.vdi" --resize 40000
```

2. 进入虚拟机的系统, 扩容系统盘
- (linux)
```
su -
#please input root password here
cfdisk
```
 - (windows)
```
    [ctrl+r] + compmgmt.msc + 磁盘管理 + 扩展卷
```
 


1. 此时, 可以用lsblk查看到磁盘已经扩容了, 但是用df -h看的话还没有扩容. 这是因为, 我们还没有将文件系统扩容到整个磁盘.
```
resize2fs /dev/sdax
```