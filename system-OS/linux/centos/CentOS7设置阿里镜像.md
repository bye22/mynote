## 1. 备份原来的[yum](https://www.baidu.com/s?wd=yum&tn=24004469_oem_dg&rsv_dl=gh_pl_sl_csd)源

```
sudo cp /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak 
```

## 2.设置aliyun的yum源

```
sudo wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo 
```

## 3.添加EPEL源

EPEL（http://[fedora](https://www.baidu.com/s?wd=fedora&tn=24004469_oem_dg&rsv_dl=gh_pl_sl_csd)project.org/wiki/EPEL）是由 Fedora 社区打造，为 RHEL 及衍生发行版如 CentOS、Scientific Linux 等提供高质量软件包的项目。装上 EPEL后，可以像在 Fedora 上一样，可以通过 yum install package-name，安装更多软件。

```
sudo wget -P /etc/yum.repos.d/ http://mirrors.aliyun.com/repo/epel-7.repo 
```

## 4.清理缓存并生成新的缓存

```
sudo yum clean all  
sudo yum makecache  
```
