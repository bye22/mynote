# 已解决

```
yay -S sof-firmware
reboot

pulseaudio -k
pulseaudio
```
---


# 方法1
amixer -D pulse sset Master toggle

# 方法2
rm -R .config/pulse/
sudo pacman -S pulseaudio

# 方法3
sudo gpasswd -a $USER audio
sudo killall pulseaudio

# 方法4
pulseaudio --check
pulseaudio --kill
pulseaudio --start

# 方法5
systemctl --user restart pulseaudio.service
systemctl --user restart pulseaudio.socket

# 排查

$ aplay -l

$ aplay -L

$ lspci

