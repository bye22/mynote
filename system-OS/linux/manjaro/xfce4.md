# 安装xfce4组

```zsh
    pacman -Sg xfce4
    sudo pacman  -S xfce4
```

# xfwm问题记录

```bash
xfwm4 --replace
```
---
(xfwm4:3000): Gtk-WARNING **: 15:30:56.581: Theme parsing error: gtk.css:2:33: Failed to import: 打开文件 /home/cogs/.config/gtk-3.0/window_decorations.css 时出错：没有那个文件或目录
Gtk-Message: 15:30:56.597: <font color='red'>Failed to load module "colorreload-gtk-module"</font>
Waiting for current window manager (Xfwm4) on screen :0.0 to exit: Done

# fix

```
locate libcolorreload-gtk-module.so
```

---

# 可使用 loginctl 来查看用户会话的状态。

```
 loginctl show-session $XDG_SESSION_ID
```

---

# 配置 sddm (Simple Desktop Display Manager)

```
 sudo pacman -S sddm-config-editor-git
 ```