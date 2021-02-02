# fcitx5
[fcitx5主题配置git](https://github.com/hosxy/Fcitx5-Material-Color)

```zsh
sudo pacman -S fcitx5-git fcitx5-chinese-addons-git fcitx5-chewing fcitx5-pinyin-zhwiki fcitx5-pinyin-moegirl fcitx5-config-qt-git fcitx5-gtk-git fcitx5-qt4-git fcitx5-qt5-git
```

update 1.1 version
```zsh
sudo pacman -S fcitx5-git fcitx5-chinese-addons-git fcitx5-chewing fcitx5-pinyin-zhwiki fcitx5-pinyin-moegirl  fcitx5-gtk-git
```

```zsh
nvim .xprofile
```

```zsh
export LC_ALL=zh_CN.UTF-8
export GTK_IM_MODULE=fcitx5
export QT_IM_MODULE=fcitx5
export XMODIFIERS="@im=fcitx5"
```

# 手动安装(皮肤主题)
```zsh
mkdir -p ~/.local/share/fcitx5/themes/Material-Color
git clone https://github.com/hosxy/Fcitx5-Material-Color.git ~/.local/share/fcitx5/themes/Material-Color

cd ~/.local/share/fcitx5/themes/Material-Color
ln -sf ./theme-blue.conf  theme.conf
```
Tips1：第一次使用时必须设置一种配色方案(不然会打回原形)，因为一些原因不方便设置一个默认的配色方案
Tips2：设置/切换配色方案后须重启输入法以生效

# 启用主题
然后修改配置文件： `~/.config/fcitx5/conf/classicui.conf`

```zsh
# 垂直候选列表
Vertical Candidate List=False

# 按屏幕 DPI 使用
PerScreenDPI=True

# Font (设置成你喜欢的字体)
Font="思源黑体 CN Medium 13"

# 主题
Theme=Material-Color
```

# 更新：
想要更新这个皮肤很简单，打开一个终端，执行以下命令：
```zsh
cd ~/.local/share/fcitx5/themes/Material-Color
git pull
```


# 单行模式(inline_preedit)
要使用单行模式(inline_preedit),
对于fcitx5自带pinyin 请修改 `~/.config/fcitx5/conf/pinyin.conf`,
对于fcitx5-rime，请新建/修改 `~/.config/fcitx5/conf/rime.conf` ，
加入/修改以下内容：

```zsh
# 可用时在应用程序中显示预编辑文本
PreeditInApplication=True
```

注意: 修改配置文件 ~/.config/fcitx5/profile 时，请务必退出 fcitx5 输入法，否则会因为输入法退出时会覆盖配置文件导致之前的修改被覆盖，修改其他配置文件可以不用退出fcitx5输入法，重启生效