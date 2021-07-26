
# 如果有启动脚本，在脚本文件头部添加以下内容
env locale=zh_CN
export LC_ALL=zh_CN.UTF-8
export XIM="ibus"
export XMODIFIERS="@im=ibus"
export GTK_IM_MODULE="ibus"
export QT_IM_MODULE="ibus"

---

## 重启ibus输入法
ibus-daemon -rd
## idea操作：
Go to "Help | Edit Custom VM options..."
Add -Drecreate.x11.input.method=true to a new line
Restart IDE

---
## sudo vim .xprofile

export LC_ALL=zh_CN.utf8

export XMODIFIERS=@im=fcitx

export QT_IM_MODULE=xim

export GTK_IM_MODULE=xim

`fcitx -d`
