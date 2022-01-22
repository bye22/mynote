
Download Setup file : https://www.opencode.net/lsteam/xfce-...
==================================
CHAPTERS OF THIS VIDEO
==================================
00:00 - Intro
00:10 - Final Result
02:24 - Initial Setup
04:03 - Installing and Configuring themes, icons, cursors and fonts
04:05 - Installing WhiteSur-gtk-theme - https://github.com/vinceliuice/WhiteS...
05:49 - Installing WhiteSur-icon-theme - https://github.com/vinceliuice/WhiteS...
06:27 - Installing WhiteSur-cursors - https://github.com/vinceliuice/WhiteS...
07:02 - Installing Fonts
08:52 - Installing Global Menu
Install Vala-Appmenu manjaro/arch : 
pamac build vala-panel-appmenu-common-git vala-panel-appmenu-registrar-git vala-panel-appmenu-xfce-git 
sudo pacman -S appmenu-gtk-module 
Execute this command after enable vala-appmenu: 
xfconf-query -c xsettings -p /Gtk/ShellShowsMenubar -n -t bool -s true 
xfconf-query -c xsettings -p /Gtk/ShellShowsAppmenu -n -t bool -s true 
10:41 - Configuring Xfce Panel | Download Xpple Menu : https://www.pling.com/p/1529470/
16:35 -  Installing and Configuring Plank Dock
sudo pacman -S plank
19:35 -  Installing and Configuring Rofi Launcher
sudo pacman -S rofi
Source : https://github.com/adi1090x/rofi
20:29 -  Installing and Configuring Ulauncher
pamac build ulauncher
23:03 -  Installing and Configuring Conky
pamac build conky-lua-nv
sudo pacman -S jq curl
24:46 -  Installing and Configuring LightDM-Webkit2-Greeter
sudo pacman -S lightdm-webkit2-greeter
Theme : https://github.com/manilarome/lightdm-webkit2-theme-glorious
28:29 -  Installing and Configuring Picom Compositor
pamac build picom-ibhagwan-git 
30:17 -  Customize Firefox Web Browser
32:01 -  Customize Xfce terminal
pamac build zsh-theme-powerlevel10k-git
chsh -s ${which_zsh}
echo 'source /usr/share/zsh-theme-powerlevel10k/powerlevel10k.zsh-theme' >> ~/.zshrc
35:09 -  Installing Nautilus File Manager
sudo pacman -S nautilus
36:12 -  Installing Comice Control center
git clone https://github.com/libredeb/comice-control-center
sudo pacman -S util-linux gsettings-desktop-schemas wireless_tools iproute alsa-utils dbus-python
sudo pacman -S python-pip
sudo pip3 install -r requirements.txt
./comice-control-center
40:09 – RAM usage before/after setup
==================================