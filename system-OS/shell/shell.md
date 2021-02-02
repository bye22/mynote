
# 变量


```shell
echo ${your_name}
```

#  重置变量


```shell
 unset variable_name
```


# 字符串

```shell
your_name="runoob"
# 使用双引号拼接
greeting="hello, "$your_name" !"
greeting_1="hello, ${your_name} !"
echo $greeting  $greeting_1
```

```shell
string="abcd"
echo ${#string} #输出 4

string="runoob is a great site"
echo ${string:1:4} # 输出 unoo

string="runoob is a great site"
echo `expr index "$string" io`  # 输出 4
```

# 数组

```shell
数组名=(值1 值2 ... 值n)

${数组名[下标]}

echo ${array_name[@]}
```
```
多行注释
:<<!
注释内容...
注释内容...
注释内容...
!

```

|参数处理|	说明|
|:---:|:----|
|`$#`	|传递到脚本的参数个数
|`$*`	|以一个单字符串显示所有向脚本传递的参数。如"`$*`"用「"」括起来的情况、以"`$1` `$2` … `$n`"的形式输出所有参数。
|`$$`	|脚本运行的当前进程ID号
|`$!`	|后台运行的最后一个进程的ID号
|`$@`	|与`$*`相同,但是使用时加引号,并在引号中返回每个参数。如"`$@`"用「"」括起来的情况、以"`$1`" "`$2`" … "`$n`" 的形式输出所有参数。
|`$-`	|显示Shell使用的当前选项，与`set`命令功能相同。
|`$?`	|显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误。