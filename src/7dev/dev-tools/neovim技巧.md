# 基本使用
`yw`               `复制一个单词`

`%s/文本内容/替换内容` `替换文本`
*Shift + `* 大小写替换
缩进
命令模式下操作： 
`:70,80>`(70-80行光标处缩进)，向左`:70,80<`

普通模式下: `>>`向右缩进 

定位:
`:num`
定位行打开文件:
`vim +n filename`
正则匹配定位打开文件
`vim +/patten filename`

`<`	向左移动文本
`>`	向右移动文本
`}`	向前移动一个段落
`{`	向后移动一个段

`Ctrl-f`	向下翻页 (Ctrl-f / Ctrl-d)
`Ctrl-b`	向上翻页 (C-b / C-u)
`Ctrl-e`	向下滚屏 (3 Ctrl-e/j)
`Ctrl-y`	向上滚屏 (3Ctrl-y/k)
`Ctrl-c`	复制当前文件绝对路径
`Ctrl-x`	切换窗口文件
`Ctrl-Shift-Up`	向上移动当前行
`Ctrl-Shift-Down`	向下移动当前

Ctrl-a
**`**

---
**组合**
## 删除成对符号包裹范围内的字符
`ci "`

## 复制成对符号包裹内字符
`cy "`

## 查找到：为止，并删除
`df:`

## 查找到：位置，并复制
`ydf:`


## F2 切换相对行， V + [num] 选中num 行

`V10`

---
## vim下编辑readonly文件解决方案
```bash
:w !sudo tee %
```
>加载文件(L)
---

# vim在系统剪切板的复制与粘贴
vim是否支持clipboard

```
    vim --version | grep clipboard
    sudo apt install vim-gtk
    sudo pacman -S xsel | sudo pacman -S xclip
```

clipboard前面有一个小小的减号

# vim的复制粘贴
    w 跳转到下个word，W：跳转到上个word
    f  某行正向查找并跳转    F: 反向....

    yy   复制一行
    dd   删除一行

    p就是在当前光标后粘贴，P就是在当前光标前粘贴

    gp，和p的功能基本一致，只是粘贴完，它会把光标移动至粘贴内容之后；gP同理

    
    :pu[t] ，注意，这个是在命令界面输入的pu/put，它的意思是把x寄存器的内容粘贴到下一行

**基本操作**

    :reg

    "ap      粘贴字母a寄存器内容
    "1y      把选取内容复制到数字寄存器1

    "+y    复制到系统剪贴板
    "+p    粘贴
    "+gp  粘贴并且移动光标到粘贴内容后

`q` 快捷键
`q /` 快捷键，打开命令行窗口
`q ?` 快捷键，打开命令行窗口
`q :` 快捷键，打开命令行窗口

**vim ~/.vimrc**
    "使用ctrl+c  和ctrl+v
    nmap <c-v> "+gp
    nmap <c-c> "+y

    
    "自定义控制键
    let mapleader=","
    nmap <leader>c "+y
    nmap <leader>v "+gp

---

# **nerd图标字体**
`sudo pacman -S nerd-fonts-hack nerd-fonts-mplus

# 安装插件管理器
```
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
``
