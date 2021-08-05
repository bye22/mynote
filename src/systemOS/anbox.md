$ sudo modprobe ashmem_linux
$ sudo modprobe binder_linux


$ snap install --devmode --beta anbox
$ snap refresh --beta --devmode anbox

# On Ubuntu
$ sudo apt install android-tools-adb

# On Fedora
$ sudo dnf install android-tools

$ adb install my-app.apk

$ anbox.appmgr

$ sudo snap restart anbox.container-manager

systemctl status anbox-container-manager.service