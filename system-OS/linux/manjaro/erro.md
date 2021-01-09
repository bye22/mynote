# deepin-wine-wechat
错误： Cannot find the strip binary required for object file stripping.
pacman -S binutils

错误： Cannot find the fakeroot binary. ==> 错误： Cannot find the strip binary required for object fil...

解决方法：因为没安装 fakeroot、binutils 等打包基本工具，所以pacman -S base-devel 装一下。

问题症状：错误： Cannot find the fakeroot binary. ==> 错误： Cannot find the strip binary required for object file stripping. ==> 错误：Makepkg 无法构建 deepin-wine-wechat.
