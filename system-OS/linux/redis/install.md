# 下载
```
$ wget http://download.redis.io/releases/redis-6.0.4.tar.gz
```
# make
```
$ tar xzf redis-6.0.4.tar.gz
$ cd redis-6.0.4
$ make
```
# make报错
```
In file included from server.c:30:0:
server.h:1022:5: error: expected specifier-qualifier-list before ‘_Atomic’
     _Atomic unsigned int lruclock; /* Clock for LRU eviction */
```

请先检查gcc的版本是否低于5，如果是请先升级，可以使用以下命令：
```
sudo yum install centos-release-scl
sudo yum install devtoolset-7-gcc*
scl enable devtoolset-7 bash
```


# Run
The binaries that are now compiled are available in the src directory. Run Redis with:
```
$ src/redis-server
```

# Using
You can interact with Redis using the built-in client:

```
$ src/redis-cli
redis> set foo bar
OK
redis> get foo
"bar"
```

2.第二种方式 （永久方式）
需要永久配置密码的话就去redis.conf的配置文件中找到requirepass这个参数，如下配置：

修改redis.conf配置文件　　

# requirepass foobared
requirepass 123   指定密码123

保存后重启redis就可以了

