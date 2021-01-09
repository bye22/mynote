# vim的复制粘贴
    w 跳转到下个word，W：跳转到上个word
    f  某行正向查找并跳转    F: 反向....

    yy   复制一行
    dd   删除一行

    p就是在当前光标后粘贴，P就是在当前光标前粘贴

    gp，和p的功能基本一致，只是粘贴完，它会把光标移动至粘贴内容之后；gP同理

    
    :pu[t] ，注意，这个是在命令界面输入的pu/put，它的意思是把x寄存器的内容粘贴到下一行

vim的寄存器和系统剪贴板

    ：help  registers

    根据官方手册：vim有9种寄存器

    There are nine types of registers:                      registers E354
    1. The unnamed register ""
    2. 10 numbered registers "0 to "9
    3. The small delete register "-
    4. 26 named registers "a to "z or "A to "Z
    5. four read-only registers ":, "., "% and "#
    6. the expression register "=
    7. The selection and drop registers "*, "+ and "~
    8. The black hole register "_
    9. Last search pattern register "/

    1.无名（unnamed）寄存器：""，缓存最后一次操作内容；

    2.数字（numbered）寄存器："0 ～"9，缓存最近操作内容，复制与删除有别, "0寄存器缓存最近一次复制的内容，"1-"9缓存最近9次删除内容

    3.行内删除（small delete）寄存器："-，缓存行内删除内容；

    4.具名（named）寄存器："a ～ "z或"A - "0Z，指定时可用；

    5.只读（read-only）寄存器：":,".,"%,"#，分别缓存最近命令、最近插入文本、当前文件名、当前交替文件名；

    6.表达式（expression）寄存器："=，只读，用于执行表达式命令；

    7.选择及拖拽（selection and drop）寄存器："*,"+,"~，存取GUI选择文本，可用于与外部应用交互，使用前提为系统剪切板（clipboard）可用；

    8.黑洞（black hole）寄存器："_，不缓存操作内容（干净删除）；

    9.模式寄存器（last search pattern）："/，缓存最近的搜索模式。

基本操作

    :reg

    "ap      粘贴字母a寄存器内容
    "1y      把选取内容复制到数字寄存器1

    "+y    复制到系统剪贴板
    "+p    粘贴
    "+gp  粘贴并且移动光标到粘贴内容后

vim ~/.vimrc
    "使用ctrl+c  和ctrl+v
    nmap <c-v> "+gp
    nmap <c-c> "+y

    
    "自定义控制键
    let mapleader=","
    nmap <leader>c "+y
    nmap <leader>v "+gp
    
# vim在系统剪切板的复制与粘贴
vim是否支持clipboard

```
    vim --version | grep "clipboard"
```

clipboard前面有一个小小的减号