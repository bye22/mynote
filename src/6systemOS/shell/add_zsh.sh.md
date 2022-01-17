#!/bin/bash
echo "正在安装zsh..."
sudo yum install zsh -y
echo "正在安装oh-my-zsh开源插件..."
sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"

