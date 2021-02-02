sudo pacman -S fcitx-googlepinyin fcitx-configtool

sudo vim ~/.xprofile

sudo vim ~/etc/profile
export LC_ALL=zh_CN.UTF-8
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS="@im=fcitx"

sudo pacman -S fcitx fcitx-rime fcitx-configtool fcitx-qt5