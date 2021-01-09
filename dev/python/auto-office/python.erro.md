# 错误

1. 编码错误
    a. Non-ASCII character 'xe5' in file报错问题
中文错误

## 解决方案
#coding=utf-8
注：此语句一定要添加在源代码的第一行。

    b. UnicodeDecodeError: 'ascii' codec can't decode byte 0xe5 in position 5: ordinal not in range(128)

import sys
reload(sys)
sys.setdefaultencoding('utf8')

2. python中出现IndentationError: unexpected indent的解决办法

## 解决：
    1.格式对齐
    2.统一对齐不可见符号 （Tab或Space）