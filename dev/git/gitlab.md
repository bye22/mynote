下载原有gitlab源码
git clone http://gitlab.**.com/projectName
gitlab地址替换成为新gitlab地址
git remote set-url origin http://gitlab.**.com/newProjectName
本地推送到远程-可以在sourceTree中进行推送
git push origin --all 推送主干和分支
git push --tags 推送标签
查看远程gitlab地址
git remote -v

git配置过程中fatal:拒绝合并无关的历史
git branch --set-upstream-to=origin/master master
git pull --allow-unrelated-histories    (忽略版本不同造成的影响)
git merge localbranch

git remote: HTTP Basic: Access denied 错误解决办法
git config –-system –-unset credential.helper 



