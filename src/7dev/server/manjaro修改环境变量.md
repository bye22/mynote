arch Linux JAVA环境配置

# vim etc/environment

CLASSPATH=.://opt/java/lib
JAVA_HOME=/opt/java


查看

archlinux-java status
设置默认
sudo archlinux-java set java-8-jdk

vim快捷键运行
map<F6> :call CompileRunGcc()<CR>

```
func! CompileRunGcc()

•     exec "w"

•     if &filetype == 'c'

•         exec '!clang % -o %<'

•         exec '!time ./%<'

•     elseif &filetype == 'cpp'

•         exec '!clang++ % -o %<'

•         exec '!time ./%<'

•     elseif &filetype == 'python'

•         exec '!time python %'

•     elseif &filetype == 'sh'

•         :!time bash %

•     elseif &filetype == 'java'

•         exec '!java %<'

•     endif

 endfunc 
```