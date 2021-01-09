# Centos8配置网络

## 原配置文件

```shell
/etc/sysconfig/network-scripts
```

```shell
# 网卡配置文件按默认配置
TYPE=Ethernet
PROXY_METHOD=none
BROWSER_ONLY=no
BOOTPROTO=dhcp
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
IPV6_ADDR_GEN_MODE=stable-privacy
NAME=ens33
UUID=e4987998-a4ce-4cef-96f5-a3106a97f5bf
DEVICE=ens33
ONBOOT=no  #如果使用dhcp分配ip的话，只需要将这里no改为yes，然后重启网络服务就行
```

## 配置静态ip

```shell
TYPE=Ethernet
PROXY_METHOD=none
BROWSER_ONLY=no
BOOTPROTO=static   #将dhcp修改为stati表示使用静态ip
DEFROUTE=yes
IPADDR=192.168.128.129   #设置IP地址
NETMASK=255.255.255.0    #设置子网掩码
GATEWAY=192.168.128.1    #设置网关
DNS1=114.114.114.114     #设置dns
IPV4_FAILURE_FATAL=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
IPV6_ADDR_GEN_MODE=stable-privacy
NAME=ens33
UUID=e4987998-a4ce-4cef-96f5-a3106a97f5bf
DEVICE=ens33
ONBOOT=yes  #将no改为yes
```

## 重启网络服务

`nmcli c reload` 命令重启网络服务，网络这块算是`centos8`改动较大的一块了

网络管理一般使用 nmclli c