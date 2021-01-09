git 本地保存账号密码
如果https的话,每次都用输入账号密码很繁琐
解决方法，在本地的工程文件夹的.git下打开config文件
添加：

`[credential]
     helper = store`

再输入一次用户名密码后就可以保存住了。

设置记住密码（默认15分钟）：


```
git config --global credential.helper cache
```
如果想自己设置时间，可以这样做：


```
git config credential.helper 'cache --timeout=3600'
```
这样就设置一个小时之后失效


长期存储密码：


```
git config --global credential.helper store
```
增加远程地址的时候带上密码也是可以的。(推荐)



从仓库的config的里面修改url，后面加上密码


```
http://yourname:password@git.oschina.net/name/project.git
```


git设置用户名密码

设置git用户名／邮箱


```bash
git config --global user.name [username]

git config --global user.email [email]
```

git保存用户名密码
1.使用如下命令，修改config文件即可保存


```bash
echo "[credential]" >> .git/config

echo "    helper = store" >> .git/config
```
2.直接修改.git/config文件



在linux/mac下可以直接使用vim工具修改config文件



```bash
$ vim .git/config
```


##修改成如下


```
[core]

    repositoryformatversion = 0

    filemode = true

    bare = false

    logallrefupdates = true

[remote "origin"]

    url = https://github.com/Miss-you/kernel-netfilter-sample-code.git

    fetch = +refs/heads/*:refs/remotes/origin/*

[branch "master"]

    remote = origin

    merge = refs/heads/master
```

##主要是后面这两行，如果不想保存，则删除即可
```
[credential]

    helper = store
```


##保存


git config查看配置 
`git config --list`


