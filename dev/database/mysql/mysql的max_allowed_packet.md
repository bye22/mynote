mysql的max_allowed_packet属性修改后无效-解决思路

值修改为：max_allowed_packet=20971520，保存重启mysql ，OK了

结论：有些服务器下的mysql由于某些原因可能无法将M转为k。

另外，如果使用docker 容器的mysql ，并且把mysql容器的配置文件目录映射到宿主机本地目录，也会报以上异常；

主要原因为：宿主机的本地目录权限不够；

用命令：chmod * 777 -R ；修改宿主机目录权限后，此问题不在出现。