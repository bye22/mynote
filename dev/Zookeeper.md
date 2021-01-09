# Zookeeper 安装、配置、使用
## 1.安装与配置过程
    解压：tar -zxvf zookeeper-3.4.10.tar.gz -C /usr/local
重命名：mv zookeeper-3.4.10/ zookeeper
修改环境变量 vim /etc/profile

```

#ZOOKEEPER配置
export ZOOKEEPER_HOME=/usr/local/zookeeper
export PATH=$PATH:$ZOOKEEPER_HOME/bin

```

刷新配置：source /etc/profile
到zookeeper下修改配置文件 cd /usr/local/zookeeper/conf
修改配置文件名称：mv zoo_sample.cfg zoo.cfg
(修改两处，vim zoo.cfg )
dataDir=/usr/local/zookeeper/data
最后面添加：
server.0=192.168.56.200:2888:3888
server.1=192.168.56.201:2888:3888
server.2=192.168.56.202:2888:3888
服务器标识配置
创建文件夹：mkdir /usr/local/zookeeper/data
创建文件myid并填写内容为0：vi myid (内容为服务器标识 ： 0)
把上面配置好的整个目录zookeeper拷贝至另外两台服务器：
 scp -r zookeeper/ 192.168.56.201:/usr/local
 scp -r zookeeper/ 192.168.56.202:/usr/local
修改另外两台服务器以下两个内容

/etc/profile环境变量配置
myid文件里的服务器标识相应的改为1和2
## 启动zookeeper
zkServer.sh start (注意这里3台机器都要进行启动)
启动后，jps可以查看到zk服务进程

查看状态
状态：zkServer.sh status(在三个节点上检验zk的mode,一个leader和俩个follower)

3.zoo.cfg配置文件详解
tickTime：基本事件单元，以毫秒为单位。这个时间是作为 Zookeeper 服务器之间或客户端与服务器之间维持心跳的时间间隔，也就是每隔 tickTime时间就会发送一个心跳。
dataDir：存储内存中数据库快照的位置，顾名思义就是 Zookeeper 保存数据的目录，默认情况下，Zookeeper 将写数据的日志文件也保存在这个目录里。
clientPort：这个端口就是客户端连接 Zookeeper 服务器的端口，Zookeeper 会监听这个端口，接受客户端的访问请求。
initLimit：这个配置项是用来配置 Zookeeper 接受客户端初始化连接时最长能忍受多少个心跳时间间隔数，当已经超过 10 个心跳的时间（也就是 tickTime）长度后 Zookeeper 服务器还没有收到客户端的返回信息，那么表明这个客户端连接失败。总的时间长度就是 10*2000=20 秒。
syncLimit：这个配置项标识 Leader 与 Follower 之间发送消息，请求和应答时间长度，最长不能超过多少个 tickTime 的时间长度，总的时间长度就是 5*2000=10 秒
server.A = B:C:D
A表示这个是第几号服务器
B 是这个服务器的 ip 地址
C 表示的是这个服务器与集群中的 Leader 服务器交换信息的端口
D 表示的是万一集群中的 Leader 服务器挂了，需要一个端口来重新进行选举，选出一个新的 Leader

