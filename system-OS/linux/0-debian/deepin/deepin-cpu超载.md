sudo apt install i7z
sudo i7z

查看CPU频率的实时结果，发现居然时因为自动降频失效造成CPU发热，从而使风扇狂响。

解决方法：

sudo gedit /etc/default/grub

编辑grub文件，其中两行改为如下：

GRUB_CMDLINE_LINUX="splash quiet "
GRUB_CMDLINE_LINUX_DEFAULT="intel_pstate=disable"

保存退出后更新一下grub

sudo update-grub

然后，重启系统。
再用i7z查看，已经能够自动降频了。