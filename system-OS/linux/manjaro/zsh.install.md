# via curl
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# via wget
sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"


# 想要卸载oh-my-zsh 输入以下命令
uninstall_oh_my_zsh


# Changing your default shell

To list all installed shells, run:
```
$ chsh -l
```

And to set one as default for your user do:
```
$ chsh -s full-path-to-shell
```