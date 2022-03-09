1. 生成一个新的SSH KEY

```shell
mkdir -p ~/.ssh && cd ~/.ssh
ssh-keygen -t rsa -C "new_personnal_publicKey"

```
~/.ssh/id_rsa_new.pub -> Github

```
vim ~/.ssh/config

```

```
Host github-personal
HostName github.com
User git
IdentityFile ~/.ssh/id_rsa_personal
```

```shell
git remote -v 

git remote set-url origin  github-personal:USER/RemoteName.git

ssh -T github-personal
ssh -T git@github.com

git remote -v
```


## 补充:
github账户如果还是显示之前id_rsa密钥账户的话请把你的密钥加入sshAgent代理中

    添加你的ssh密钥到ssh-agent中

# start the ssh-agent in the background
eval "$(ssh-agent -s)"
Agent pid 59566

如果你的密钥不是系统默认的RSA文件名id_rsa，比如像我一样另外创了一对公钥/密钥id_rsa_personal，那么就把他们添加进去，注意：密钥文件是不带扩展名的，公钥扩展名是.pub，代表publicKey，
apple:.ssh apple$ eval "$(ssh-agent -s)"
Agent pid 19795
//添加密钥 id_rsa_personal
apple:.ssh apple$ ssh-add id_rsa_personal
Identity added: id_rsa_personal (github-personal)
//添加默认密钥 id_rsa
apple:.ssh apple$ ssh-add id_rsa
//密钥有密码的话就会要你提示输入 passphrase
Enter passphrase for id_rsa: 
//测试用密钥isa是否连接成功github
apple:.ssh apple$ ssh -T git@github.com
Hi hbxn740150254! You 've successfully authenticated, but GitHub does not provide shell access.
//测试密钥id_rsa_personal是否连接成功github
apple:.ssh apple$ ssh -T git@github-personal
Hi FaxeXian! You've successfully authenticated, but GitHub does not provide shell access.
