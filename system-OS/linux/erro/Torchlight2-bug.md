 
与系统库冲突导致的问题
Mathematica 软件包包含了一系列其自有的库，存放在 <INSTALL_DIR>/SystemFiles/Libraries/Linux-x86-64 里面。它们可能会导致一些兼容性问题，并且可能需要将某些库回退到系统现有版本。

Symbol lookup error: /usr/lib/libfontconfig.so.1: undefined symbol: FT_Done_MM_Var
强制 Mathematica 使用系统自有的 freetype 库。

# cd <INSTALL_DIR>/SystemFiles/Libraries/Linux-x86-64
# mv libfreetype.so.6 libfreetype.so.6.old

#错误信息
0209/134205.702616:ERROR:object_proxy.cc(619)] Failed to call method: org.kde.KWallet.isEnabled: object_path= /modules/kwalletd5: org.freedesktop.DBus.Error.NoReply: Message recipient disconnected from message bus without replying
[0209/134205.702693:ERROR:kwallet_dbus.cc(100)] Error contacting kwalletd5 (isEnabled)
[0209/134205.703024:ERROR:object_proxy.cc(619)] Failed to call method: org.kde.KLauncher.start_service_by_desktop_name: object_path= /KLauncher: org.freedesktop.DBus.Error.ServiceUnknown: The name org.kde.klauncher was not provided by any .service files
[0209/134205.703038:ERROR:kwallet_dbus.cc(72)] Error contacting klauncher to start kwalletd5
[0209/134205.765645:ERROR:object_proxy.cc(619)] Failed to call method: org.kde.KWallet.close: object_path= /modules/kwalletd5: org.freedesktop.DBus.Error.NoReply: Message recipient disconnected from message bus without replying
[0209/134205.765677:ERROR:kwallet_dbus.cc(414)] Error contacting kwalletd5 (close)
没有解决
