[root@localhost crossover-deepin_16.0.6-1_i386]# sudo rpm -ivh crossover-deepin-16.0.6-2.i386.rpm 
错误：依赖检测失败：
        libcrypt.so.1 被 crossover-deepin-16.0.6-2.i386 需要
        libcxjpeg.so.9 被 crossover-deepin-16.0.6-2.i386 需要
        libcxjpeg.so.9()(64bit) 被 crossover-deepin-16.0.6-2.i386 需要
        libnsl.so.1 被 crossover-deepin-16.0.6-2.i386 需要
        libnsl.so.1(GLIBC_2.0) 被 crossover-deepin-16.0.6-2.i386 需要
        libwine.so.1 被 crossover-deepin-16.0.6-2.i386 需要
        libwine.so.1()(64bit) 被 crossover-deepin-16.0.6-2.i386 需要
        libwine.so.1(WINE_1.0) 被 crossover-deepin-16.0.6-2.i386 需要
        libwine.so.1(WINE_1.0)(64bit) 被 crossover-deepin-16.0.6-2.i386 需要
[root@localhost crossover-deepin_16.0.6-1_i386]# sudo dnf install libcrypt.so.1
 
 
 
 
 错误：依赖检测失败：
        libcxjpeg.so.9 被 crossover-deepin-16.0.6-2.i386 需要
        libcxjpeg.so.9()(64bit) 被 crossover-deepin-16.0.6-2.i386 需要
        libwine.so.1()(64bit) 被 crossover-deepin-16.0.6-2.i386 需要
        libwine.so.1(WINE_1.0)(64bit) 被 crossover-deepin-16.0.6-2.i386 需要
