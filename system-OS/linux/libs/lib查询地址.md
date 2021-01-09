
[依赖包查询网站](https://pkgs.org/)

<font color =red>
 :: PGP 密钥需要导入:</p>
 -> 4B286694DE99D517AA8DFF2D6656C593E5158D1A, 需要: ddd</p>
==> 导入？ [Y/n] Y</p>
:: 正在用 gpg 导入密钥...</p>
gpg: 从公钥服务器接收失败：一般错误</p>
导入密钥时出现问题</p>
</font>

<font color=green>
 -> 8AAA779B597B405BBC329B6376CF47B8A77C5329, 需要: lib32-net-snmp</p>
 -> 27CAA4A32E371383A33ED0587D5F9576E0F81533, 需要: lib32-net-snmp</p>
 -> D0F8F495DA6160C44EFFBF10F07B9D2DACB19FD6, 需要: lib32-net-snmp</p>
 -> 7C4AFD61D8AAE7570796A5172209D6902F969C95, 需要: lib32-libgphoto2</p>
 -> 5558F9399CD7836850553C6EC28E7847ED70F82D, 需要: lib32-pciutils</p>




应该是https证书的问题，可以换个keyserver手动导入。 

```
gpg --keyserver p80.pool.sks-keyservers.net --recv-keys 4B286694DE99D517AA8DFF2D6656C593E5158D1A
```

国内可用key server列表：
keyserver.ubuntu.com
pgp.mit.edu
subkeys.pgp.net
www.gpg-keyserver.de