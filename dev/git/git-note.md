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


# Git设置全局忽略文件

```
touch ~/.gitignore_global
git config --global core.excludesfile ~/.gitignore_global
```

# git cz使用(替代git commit 实现代码快速提交。)

1. 安装
```
npm install -g commitizen

npm install -g cz-conventional-changelog

echo '{ "path": "cz-conventional-changelog" }' > ~/.czrc
```

---

> 项目中使用commitizen生成符合AngularJS规范的提交说明(可选)

初始化命令主要进行了3件事情:

在项目中安装cz-conventional-changelog 适配器依赖

将适配器依赖保存到package.json的devDependencies字段信息

在package.json中新增config.commitizen字段信息，主要用于配置cz工具的适配器路径

```

cd /[path]/[project]/

npm init --yes

commitizen init cz-conventional-changelog --save --save-exact --force


```
---
2. 使用

```
git cz

```

说明:
    三个部分:
    ```
    <Header> <Body> <Footer>
    ```

Header -| type
        | scope
        | subject

```
<type>(<scope>): <subject>
```


|  值  |  描述  |  表头3  |  表头4  |
| :-----: | :----: | :----: | :----: |
|  feat  |  新增一个功能  |    |    |
|  fix  |  修复一个bug  |    |    |
|  docs  |  文档变更  |    |    |
|  style  |  代码格式(不影响功能,例如空格,分号等格式修正)  |    |    |
|  refactor  |  代码重构  |    |    |
|  perf  |  改善性能  |    |    |
|  test  |  测试  |    |    |
|  build  |  变更项目构建或外部依赖(例如scopes:webpack,gulp,npm,pom等)  |    |    |
|  ci  |  更改持续集成软件的配置文件和package的script命令,例如scopes:Travis,Circle等  |    |    |
|  chore  |  变更构建流程或辅助工具  |    |    |
|  revert  |  代码回退  |    |    |

scope: 说明commit影响范围.

subject : commit简短描述.

---

Body : 
commit详细描述,说明代码提交的详细说明.

---

Footer : 
代码提交不兼容变更或关闭缺陷,则Footer必须,否则可以省略.
不兼容变更: 
        当前代码与上一个版本不兼容,则Footer以BREAKING CHANGE开头,
        后面是对变更的描述,以及变动的理由和迁移方法.
关闭缺陷 :
         如果当前提交是针对特定的issue，那么可以在Footer部分填写需要关闭的单个issue 或一系列issues.
---



