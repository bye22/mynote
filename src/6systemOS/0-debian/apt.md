<pre>常用命令：
  list - 根据名称列出软件包
  search - 搜索软件包描述
  show - 显示软件包细节
  install - 安装软件包
  reinstall - 重新安装软件包
  remove - 移除软件包
  autoremove - 卸载所有自动安装且不再使用的软件包
  update - 更新可用软件包列表
  upgrade - 通过 安装/升级 软件来更新系统
  full-upgrade - 通过 卸载/安装/升级 来更新系统
  edit-sources - 编辑软件源信息文件
  satisfy - 使系统满足依赖关系字符串</pre>

### 查看可更新软件
<pre><font color="#4E9A06"><b>bye@pop-os</b></font>:<font color="#3465A4"><b>~</b></font>$ apt list --upgradable</pre>

### 升级可用软件（All） 
<pre><font color="#4E9A06"><b>bye@pop-os</b></font>:<font color="#3465A4"><b>~</b></font>$ sudo apt upgrade</pre>

## apt-fast 多线程apt-get工具安装
sudo add-apt-repository ppa:apt-fast/stable
sudo apt-get update
sudo apt-get -y install apt-fast
