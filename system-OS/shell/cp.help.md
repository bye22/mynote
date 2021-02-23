# Linux基础动作

## cp拷贝
---
用法：cp [选项]... [-T] 源文件 目标文件
　或：cp [选项]... 源文件... 目录
　或：cp [选项]... -t 目录 源文件...
将指定<源文件>复制至<目标文件>，或将多个<源文件>复制至<目标目录>。

必选参数对长短选项同时适用。
  -a, --archive			等于-dR --preserve=all
      --attributes-only	仅复制属性而不复制数据      --backup[=CONTROL		为每个已存在的目标文件创建备份
  -b				类似--backup 但不接受参数
      --copy-contents		在递归处理是复制特殊文件内容
  -d				等于--no-dereference --preserve=links
  -f, --force                  如果有已存在的目标文件且无法打开，则将其删除并重试
                                 （该选项在与 -n 选项同时使用时将被忽略）
  -i, --interactive            覆盖前询问（使前面的 -n 选项失效）
  -H                           跟随源文件中的命令行符号链接
  -l, --link                   硬链接文件以代替复制
  -L, --dereference            总是跟随源文件中的符号链接
  -n, --no-clobber		不要覆盖已存在的文件(使前面的 -i 选项失效)
  -P, --no-dereference		不跟随源文件中的符号链接
  -p				等于--preserve=模式,所有权,时间戳
      --preserve[=属性列表	保持指定的属性(默认：模式,所有权,时间戳)，如果
					可能保持附加属性：上下文、链接、xattr 等
      --sno-preserve=属性列表	不保留指定的文件属性
      --parents			复制前在目标目录创建来源文件路径中的所有目录
  -R, -r, --recursive		递归复制目录及其子目录内的所有内容
      --reflink[=WHEN]		控制克隆/CoW 副本。请查看下面的内如。
      --remove-destination	尝试打开目标文件前先删除已存在的目的地
					文件 (相对于 --force 选项)
      --sparse=WHEN		控制创建稀疏文件的方式
      --strip-trailing-slashes	删除参数中所有源文件/目录末端的斜杠
  -s, --symbolic-link		只创建符号链接而不复制文件
  -S, --suffix=后缀		自行指定备份文件的后缀
  -t,  --target-directory=目录	将所有参数指定的源文件/目录
                                           复制至目标目录
  -T, --no-target-directory	将目标目录视作普通文件
  -u, --update			只在源文件比目标文件新，或目标文件
					不存在时才进行复制
  -v, --verbose		显示详细的进行步骤
  -x, --one-file-system	不跨越文件系统进行操作
  -Z                           设置目标文件的 SELinux 安全上下文为默认类型
      --context[=上下文]       类似 -Z；如果指定了上下文，则将 SELinux 或
                                 SMACK 安全上下文设置为指定值
      --help		显示此帮助信息并退出
      --version		显示版本信息并退出

默认情况下，源文件的稀疏性仅仅通过简单的方法判断，对应的目标文件目标文件
也将设为稀疏。这是因为默认情况下使用了--sparse=auto 参数。如果明确使用
--sparse=always 参数，则不论源文件是否包含足够长的 0 序列，都会将目标文件
创建为稀疏文件。使用 --sparse=never 参数可以禁止创建稀疏文件。

当指定了 --reflink[=always] 参数时，将进行轻量级复制，此时数据块只在被修改时
进行复制，如果无法如此操作则复制将会失败。或者如果指定了 --reflink=auto，程序
将会回退到标准复制操作。使用 --reflink=never 可以确保永远进行标准复制。

备份文件的后缀为"~"，除非以--suffix 选项或是 SIMPLE_BACKUP_SUFFIX
环境变量指定。版本控制的方式可通过--backup 选项或 VERSION_CONTROL 环境
变量来选择。以下是可用的变量值：

  none, off       不进行备份(即使使用了--backup 选项)
  numbered, t     备份文件加上数字进行排序
  existing, nil   若有数字的备份文件已经存在则使用数字，否则使用普通方式备份
  simple, never   永远使用普通方式备份

有一个特别情况：如果同时指定--force 和--backup 选项，而源文件和目标文件
是同一个已存在的一般文件的话，cp 会将源文件备份。

GNU coreutils 在线帮助：<https://www.gnu.org/software/coreutils/>
请向 <http://translationproject.org/team/zh_CN.html> 报告任何翻译错误
完整文档 <https://www.gnu.org/software/coreutils/cp>
或者在本地使用：info '(coreutils) cp invocation'
