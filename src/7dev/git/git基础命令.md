
# git基础命令

git init：初始化一个git仓库

git init newDir

git clone：clone一个git仓库

git clone [url] [directory]

Git 基本指令的使用
下面介绍一下git中常用的几种命令：

git config：配置信息

```shell
git config --global user.name '你的用户名'
git config --global user.email '你的邮箱'
```

git add：添加文件到缓存命令
git status：查看文件的状态命令
git diff：查看更新的详细信息命令
git commit：提交命令

```shell
git commit -am "第一次版本提交"
```

git reset HEAD：取消缓存命令
git rm：删除命令
git mv：移动或重命名命令

# Git的分支管理

git branch：查看分支命令
git branch (branchname)：创建分支命令
git checkout (branchname)：切换分支命令
git merge：合并分支命令
git branch -d (branchname)：删除分支命令