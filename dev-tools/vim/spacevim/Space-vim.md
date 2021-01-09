# 安装
    curl -sLf https://spacevim.org/cn/install.sh | bash -s -- -h
    curl -sLf https://spacevim.org/cn/install.sh | bash
    curl -sLf https://spacevim.org/cn/install.sh | bash -s -- --uninstall

| bash -s -- --install neovim
**nerd图标字体**
`sudo pacman -S nerd-fonts-hack nerd-fonts-mplus`


# 问题 
[vimproc] vimproc's DLL: "/home/cogs/.SpaceVim/bundle/vimproc.vim/lib/vimproc_linux64.so" is not found Please read `:help vimproc` and make it.

```zsh
:help vimproc
```

# 自动编译安装

[[plugins]]
  repo="Shougo/vimproc.vim"
  build="make"

在Vim/SpaceVim的命令模式执行: `VimProcInstall`

`:h dein-options` 查阅。
# 手动安装

git  clone https://github.com/Shougo/vimproc.vim $HOME/.SpaceVim/bundle

`$make`

# init

## cmdline
basic mode
dark powered mode

# 快捷键
## 默认
<leader> \

**更新插件**
 :SPUpdate
 **更行SpaceVim**
 :SPUpdate SpaceVim

 SpaceVim 使用 `vimfiler` 作为默认的`文件树插件`，默认的快捷键是 `F3`

## 文件树中的常用操作
文件树中主要以 `hjkl` 为核心，这类似于 vifm 中常用的快捷键：

快捷键	功能描述
`<F3>` / `SPC f t`	切换文件树
文件树内的快捷键	 
`<Left>` / `h`	移至父目录，并关闭文件夹
`<Down>` / `j`	向下移动光标
`<Up>` / `k`	向上移动光标
`<Right> / `l`	展开目录，或打开文件
l / <Enter>	打开文件
`N`	在光标位置新建文件
`dd`删除光标处文件
`.`	切换显示隐藏文件
`y y`	复制光标下文件路径至系统剪切板

`y Y`	复制光标下文件至系统剪切板
`P`	在光标位置黏贴文件
`Ctrl+r`	刷新页面

`s v`	分屏编辑该文件
`s g`	垂直分屏编辑该文件

`'`	标记光标下的文件（夹）
`V`	清除所有标记
`i`	切换至文件夹历史

`p`	预览文件
`v`	快速查看
`>`	放大文件树窗口宽度
`<`	缩小文件树窗口宽度
`g x`	使用相关程序执行该文件

## 基本

`<`	向左移动文本
`>`	向右移动文本
`}`	向前移动一个段落
`{`	向后移动一个段落

`Ctrl-f`	向下翻页 (Ctrl-f / Ctrl-d)
`Ctrl-b`	向上翻页 (C-b / C-u)
`Ctrl-e`	向下滚屏 (3 Ctrl-e/j)
`Ctrl-y`	向上滚屏 (3Ctrl-y/k)
`Ctrl-c`	复制当前文件绝对路径
`Ctrl-x`	切换窗口文件
`Ctrl-Shift-Up`	向上移动当前行
`Ctrl-Shift-Down`	向下移动当前行

## 原生功能
快捷键	功能描述
<leader> q r	原生 q 快捷键
<leader> q r/	原生 q / 快捷键，打开命令行窗口
<leader> q r?	原生 q ? 快捷键，打开命令行窗口
<leader> q r:	原生 q : 快捷键，打开命令行窗口

## 可视模式快捷键
快捷键	功能描述
<Leader> y	复制选中文本至系统剪切板
<Leader> p	粘贴系统剪切板内容至当前位置
<	向左移动文本
>	向右移动文本
<Tab>	向右移动文本
Shift-<Tab>	向左移动文本
Ctrl-Shift-Up	向上移动选中行
Ctrl-Shift-Down	向下移动选中行
Ctrl-q	Ctrl-w 退出spv

## 命令行模式快捷键
常规模式下按下 : 键后，可进入命令行模式，再次可以是下可以编辑 Vim 的命令并执行， 以下列出了命令行模式下一些常用的移动光标、删减字符的快捷键：

快捷键	功能描述
Ctrl-a	移动光标至行首
Ctrl-b	向左移动光标
Ctrl-f	向右移动光标
Ctrl-w	删除光标前词
Ctrl-u	移除光标前所有字符
Ctrl-k	移除光标后所有字符
Ctrl-c/Esc	离开命令行模式
Tab	选择下一个匹配
Shift-Tab	选择上一个匹配

