# gitlab包含历史提交记录代码迁移
git clone --bare https://username:password@gitlab.shuzhuo.com/demo.git
git push --mirror http://username:psaaword@127.0.0.1/demo.git

# reset password
sudo gitlab-rake "gitlab:password:reset"

# install gitlab

```
sudo dnf install -y curl policycoreutils openssh-server openssh-clients
# Enable OpenSSH server daemon if not enabled: sudo systemctl status sshd
sudo systemctl enable sshd
sudo systemctl start sshd

# Check if opening the firewall is needed with: sudo systemctl status firewalld
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo systemctl reload firewalld

sudo dnf install postfix
sudo systemctl enable postfix
sudo systemctl start postfix

curl -sS https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.rpm.sh | sudo bash

sudo EXTERNAL_URL="https://gitlab.example.com" dnf install -y gitlab-ce

```




一：先停止gitlab

gitlab-ctl stop

二：卸载gitlab部分（之前我是rpm安装的，这里rpm卸载）

rpm  -e  gitlab-ce

三：发现系统进程还有一个gitlab的进程

之后kill  -9  607（进程号）

四： 删除所有包含gitlab的文件及目录

find / -name gitlab | xargs rm -rf              删除所有包含gitlab的文件及目录


以上操作要是有提示说备份到XXXXXX，切换到那手动删除即可


补充：    要是gitlab是编译安装的，执行以上停止服务，灭杀相关进程，在切换到当初编译安装指向的路径（--prefix），删除下面全部文件即可，要是还有其他编译指向，同上操作即可


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



