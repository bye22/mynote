https://www.jianshu.com/p/7d00ead50e3d

free -m

sudo mkdir /swap
cd /swap

sudo dd if=/dev/zero of=swapfile bs=1G count=6

sudo watch -n 5 killall -USR1 dd

sudo mkswap -f swapfile

sudo chmod 0600 /swap/swapfile

sudo swapon /swap/swapfile

sudo nano /etc/fstab
