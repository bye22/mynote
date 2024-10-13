# DNS缓存服务 — NSCD （Name Service Cache Daemon）

一种能够缓存 passwd、group、hosts 的本地缓存服务，分别对应三个源 /etc/passwd、/etc/hosts、/etc/resolv.conf。

配置
nscd 的配置文件默认路径为`/etc/nscd.conf`。

阿里云主机的 nscd 配置信息如下：

```shell
# 日志文件
#logfile        /var/log/nscd.log
# 调试级别
debug-level     5
# 等待请求的线程数
threads         6
# 最大线程数
max-threads     128
# 运行用户
server-user     nscd
paranoia        no
# 禁用passwd缓存
enable-cache    passwd      no
# 禁用group缓存
enable-cache    group       no
# 启用hosts缓存
enable-cache    hosts       yes
# 指定缓存命中项的TTL，单位为s
positive-time-to-live   hosts   5
# 指定缓存未命中项的TTL，单位为s
negative-time-to-live   hosts       20
# 散列表大小
suggested-size  hosts       211
# 启用hosts文件的修改情况检查
check-files     hosts       yes
persistent      hosts       yes
shared          hosts       yes
# 最大缓存库大小
max-db-size     hosts       33554432

```

命令
nscd 服务默认是关闭的，通过`service nscd start`开启。

查看统计信息

```shell
$ nscd -g

nscd configuration:

              5  server debug level
 59d 17h 15m 50s  server runtime
              6  current number of threads
            128  maximum number of threads
              0  number of times clients had to wait
             no  paranoia mode enabled
           3600  restart internal
              5  reload count
hosts cache:

            yes  cache is enabled
            yes  cache is persistent
            yes  cache is shared
            211  suggested size
         216064  total data pool size
              0  used data pool size
              5  seconds time to live for positive entries
             20  seconds time to live for negative entries
              0  cache hits on positive entries
              0  cache hits on negative entries
          41794  cache misses on positive entries
          42276  cache misses on negative entries
              0% cache hit rate
              0  current number of cached values
            365  maximum number of cached values
              8  maximum chain length searched
              0  number of delays on rdlock
              0  number of delays on wrlock
              0  memory allocations failed
            yes  check /etc/hosts for changes
```

- 清除缓存

 ```shell
    当更改完域名指向后，清除dns缓存
$ nscd -i hosts
```

- 关闭服务

```shell
nscd -K
```

- 作用
开启 nscd 的 hosts 缓存服务后，每次内部接口请求不会都发起 dns 解析请求，而是直接命中 nscd 缓存散列表，从而获取对应服务器 ip 地址，这样可以在大量内部接口请求时减少接口的响应时间。
