sudo pacman-mirrors -i -c China -m rank
sudo pacman -Syy

sudo pacman -S archlinux-keyring

vim /etc/pacman.conf

[archlinuxcn]

SigLevel = Optional TrustedOnly

Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch
