# linux - 查看端口被什么程序占用
# 使用 `ss` 查看


`ss` 一般用于转储套接字统计信息。它还可以显示所有类型的套接字统计信息，包括 PACKET、TCP、UDP、DCCP、RAW、Unix 域等。


```bash
ss -lntpd | grep :22
```


tcp LISTEN 0 128 0.0.0.0:22 0.0.0.0:* users:(("sshd",pid=6806,fd=3))
tcp LISTEN 0 128 [::]:22 [::]:* users:(("sshd",pid=6806,fd=4))


通过`grep`来获取到对应的记录， 如果是本身用户可以直接查看到`pid信息`，如果是其他用户的程序一般使用`root权限`就可以查看到所有程序的进程信息。

# 使用 `netstat` 查看


`netstat` 能够显示网络连接、路由表、接口统计信息、伪装连接以及多播成员。目前netstat 已经过时了，都推荐使用ss来代替。


```bash
netstat -tnlp | grep :22
```

tcp 0 0 0.0.0.0:22 0.0.0.0:* LISTEN 6806/sshd
tcp6 0 0 :::22 :::* LISTEN 6806/sshd


同理，要查看到所有程序需要有root权限。


# 使用 lsof 查看


`lsof(list open files)`是一个列出系统上被进程打开的文件的相关信息。


```bash
lsof -i tcp:22
```

COMMAND PID USER FD TYPE DEVICE SIZE/OFF NODE NAME
sshd 6806 root 3u IPv4 147399 0t0 TCP *:ssh (LISTEN)
sshd 6806 root 4u IPv6 147401 0t0 TCP *:ssh (LISTEN)


同理，要查看到所有程序需要有root权限。


# 使用 fuser 查看


`fuser` 可以显示出当前哪个程序在使用磁盘上的某个文件、挂载点、甚至网络端口，并给出程序进程的详细信息。`fuser`只把PID输出到标准输出，其他的都输出到标准错误输出。

```bash
fuser 22/tcp
```

22/tcp: 6806


># 总结
