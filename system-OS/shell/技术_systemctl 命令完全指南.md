
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>技术|systemctl 命令完全指南</title>
 
<meta name="keywords" content="systemctl 命令完全指南" />
<meta name="description" content="Systemctl是一个systemd工具，主要负责控制systemd系统和服务管理器。 Systemd是一个系统管理守护进程、工具和库的集合，用于取代System V初始进程。Systemd的功能是用于集中管理和配置类UNIX系统。 在Linux生态系统中，Systemd被部署到了大多数的标准Linux发行版中，只有为数不多的几个发行版尚未部署。Systemd通常是所有其它守护进程的父进程，但并非总是如此。  使用Systemctl管理Linux服务 本文旨在阐明在运行systemd的系统上如何控制系统和服务。 Systemd初体验和Systemctl基础 1. 首先检查你的系统中是否安装有systemd并确定当前安 " />
<meta name="copyright" content="2005-2019 Linux.cn" />
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0" />
<meta name="applicable-device" content="pc,mobile">
<meta name="referrer" content="always">
<base href="https://linux.cn/" /><link rel="stylesheet" type="text/css" href="https://img.linux.net.cn/data/cache/style_1_common.css?yX7" />
<link rel="stylesheet" type="text/css" href="https://img.linux.net.cn/data/cache/style_1_portal_view.css?yX7" />
<link href="https://img.linux.net.cn/static/css/responsive.css?yX7" rel="stylesheet">

<script type="text/javascript">var STYLEID = '1', STATICURL = 'https://img.linux.net.cn/static/', IMGDIR = 'https://img.linux.net.cn/static/image/common', VERHASH = 'yX7', charset = 'utf-8', discuz_uid = '0', cookiepre = 'dx_516d_', cookiedomain = '.linux.cn', cookiepath = '/', showusercard = '1', attackevasive = '0', disallowfloat = '', creditnotice = '1|经验|,2|L币|,3|贡献|', defaultstyle = '', REPORTURL = 'aHR0cDovL2xpbnV4LmNuL2FydGljbGUtNTkyNi0xLmh0bWw=', SITEURL = 'https://linux.cn/', JSPATH = 'https://img.linux.net.cn/static/js/', CSSPATH = 'data/cache/style_', DYNAMICURL = '';</script>
<script src="https://img.linux.net.cn/static/js/common.js?yX7" type="text/javascript"></script>
<script src="https://img.linux.net.cn/static/js/jquery-1.11.0.min.js" type="text/javascript"></script>
<script type="text/javascript">jQuery.noConflict();</script>
<script src="https://img.linux.net.cn/static/js/jquery.plugins.js?yX7" type="text/javascript"></script>
<script src="https://img.linux.net.cn/static/js/bootstrap.min.js?yX7" type="text/javascript"></script>
<link rel="alternate" type="application/rss+xml" title="Linux 中国◆开源社区 RSS" href="/rss.xml" />
<link rel="shortcut icon" href="https://img.linux.net.cn/favicon.ico"  sizes="32x32" />
<link rel="canonical" href="https://linux.cn/article-5926-1.html" />
<script src="https://img.linux.net.cn/static/js/portal.js?yX7" type="text/javascript"></script>
</head>

<body id="nv_portal" class="pg_view" onkeydown="if(event.keyCode==27) return false;">
<div id="append_parent"></div><div id="ajaxwaitid"></div>
<div id="hd">
<div class="wp" style="box-shadow: 1px 1px 2px #666;">
<h1 id="linuxcn_logo" ><a href="https://linux.cn/" title="Linux.中国 - 开源社区"></a><style type="text/css">@-webkit-keyframes spin{100%{-webkit-transform:rotate(360deg);}}@keyframes spin{100%{transform:rotate(360deg);}}</style></h1>
<div class="p_pop h_pop" id="mn_userapp_menu" style="display: none"></div><div id="topmenu_wrapper">
<div id="topmenu">
<div id="nv">
<ul><li id="mn_N6666" ><a href="/" hidefocus="true"   style="font-weight: bold;">Linux 中国</a></li><li id="mn_P3" onmouseover="navShow('P3')"><a href="https://linux.cn/tech/" hidefocus="true"   style="color: #FFFAE5;">技术</a></li><li id="mn_P1" onmouseover="navShow('P1')"><a href="https://linux.cn/news/" hidefocus="true"   style="color: #FFFAE5;">新闻</a></li><li id="mn_P4" onmouseover="navShow('P4')"><a href="https://linux.cn/talk/" hidefocus="true"   style="color: #FFFAE5;">观点</a></li><li id="mn_P8" onmouseover="navShow('P8')"><a href="https://linux.cn/share/" hidefocus="true"   style="color: #FFFAE5;">分享</a></li><li id="mn_N1fa1" ><a href="/lctt/" hidefocus="true" target="_blank"  >LCTT</a></li></ul>
</div>
<div id="mu" class="cl">
<ul class="cl " id="snav_mn_P3" style="display:none;">
<li><a href="https://linux.cn/tech/desktop/" hidefocus="true" >桌面应用</a></li><li><a href="https://linux.cn/tech/sa/" hidefocus="true" >系统运维</a></li><li><a href="https://linux.cn/tech/program/" hidefocus="true" >软件开发</a></li><li><a href="https://linux.cn/tech/raspberrypi/" hidefocus="true" >树莓派</a></li><li><a href="https://linux.cn/tech/container/" hidefocus="true" >容器与云</a></li><li><a href="https://linux.cn/portal.php?mod=list&catid=27" hidefocus="true" >区块链</a></li></ul>
<ul class="cl " id="snav_mn_P1" style="display:none;">
<li><a href="https://linux.cn/news/express/" hidefocus="true" >新闻拍一拍</a></li></ul>
<ul class="cl " id="snav_mn_P4" style="display:none;">
<li><a href="https://linux.cn/talk/comic/" hidefocus="true" >极客漫画</a></li><li><a href="https://linux.cn/talk/ossip/" hidefocus="true" >开源智慧</a></li><li><a href="https://linux.cn/talk/interview/" hidefocus="true" >穿山甲专访</a></li><li><a href="https://linux.cn/talk/ocselected/" hidefocus="true" >开源之道</a></li><li><a href="https://linux.cn/talk/clh/" hidefocus="true" >代码英雄</a></li></ul>
<ul class="cl " id="snav_mn_P8" style="display:none;">
<li><a href="https://linux.cn/share/distro/" hidefocus="true" >Linux 发行版</a></li></ul>
<ul class="cl " id="snav_mn_userapp" style="display:none;">
</ul>
</div>
</div>
</div>
<div id="scbar" class="cl" >
<form id="scbar_form" method="post" autocomplete="off" onsubmit="searchFocus($('scbar_txt'))" action="search.php?searchsubmit=yes" target="_blank">
<input type="hidden" name="mod" id="scbar_mod" value="search" />
<input type="hidden" name="formhash" value="7ba44b27" />
<input type="hidden" name="srchtype" value="title" />
<input type="hidden" name="srhfid" value="0" />
<input type="hidden" name="srhlocality" value="portal::view" />
<table id="scbar_table" cellspacing="0" cellpadding="0" style="float:right;">
<tr>
<td class="scbar_icon_td"></td>
<td class="scbar_txt_td"><input type="text" name="srchtxt" id="scbar_txt" value="请注册后再搜索" autocomplete="off" speech /></td>
<td class="scbar_type_td"><a href="javascript:;" id="scbar_type" class="xg1" onclick="showMenu(this.id)" hidefocus="true">搜索</a></td>
<td class="scbar_btn_td"><button type="submit" name="searchsubmit" id="scbar_btn" sc="1" class="pn pnc" value="true"><strong class="xi2">搜索</strong></button></td>
<td class="scbar_hot_td">
<div id="scbar_hot">
</div>
</td>
</tr>
</table>
</form>
<span class="z titletext" style="padding: 0 10px 0 20px;">❏ 站外平台：</span>
<ul id="ext_plantform" class="cl mutag z">
<li><a class="hidefocus tsina" hidefocus="true" href="https://weibo.com/linuxcn" target="_blank" title="微博认证号：Linux中国"></a></li>
<li><a class="hidefocus tticon" hidefocus="true" href="https://www.toutiao.com/c/user/52889878622/" target="_blank" title="今日头条：Linux中国"></a></li>
<li><a class="hidefocus tticon" hidefocus="true" href="http://www.toutiao.com/c/user/3357852467/" target="_blank" title="今日头条：Linux技术"></a></li>
<li><a class="hidefocus wyicon" hidefocus="true" href="http://dy.163.com/v2/article/detail/D282EJLD0511CPOJ.html" target="_blank" title="网易号：Linux"></a></li>
<li><a class="hidefocus fbicon" hidefocus="true" href="https://www.facebook.com/linux.china/" target="_blank" title="Facebook Page：Linux中国"></a></li>
<li><a class="hidefocus zhicon" hidefocus="true" href="https://www.zhihu.com/org/linuxzhong-guo/" target="_blank" title="知乎机构号：Linux中国"></a></li>
<li><a class="hidefocus twicon" hidefocus="true" href="https://twitter.com/linux_cn" target="_blank" title="Twitter：Linux中国"></a></li>
<li><a class="hidefocus tgicon" hidefocus="true" href="https://t.me/linuxdotcn" target="_blank" title="Telegram Channel：Linux中国"></a></li>
</ul>
</div>
<br class="clear" />
<ul id="scbar_type_menu" class="p_pop" style="display: none;"><li><a href="javascript:;" rel="search">全站</a></li></ul>
<script type="text/javascript">
initSearchmenu('scbar', '');
</script>
<script type="text/javascript">
(function($){
$(window).load(function() {
$("#topmenu").affix({offset : {
top : $("#topmenu").offset().top,
bottom: 218}});
$('#topmenu_wrapper').height($("#topmenu").height());
$("#topmenu").on('affixed.bs.affix',function() {
if ($('#linuxcn_logo').is(':visible')) {
$('#mn_N6666').css({'display': 'block','width': '179px'});
$('#mn_N6666 a').css({'padding': '0 45px'});
$(this).css({'padding-left': 0,'width':'1200px'});
}
});
$("#topmenu").on('affixed-top.bs.affix',function() {
if ($('#linuxcn_logo').is(':visible')) {
$('#mn_N6666').css({'display': 'none'});
$(this).css({'padding-left': '180px','width': '1020px'});
}
});
})
})(jQuery);
</script>

</div>
</div>
<div id="wp" class="wp">

<style type="text/css">
#nv_portal .vw .h.hm {border-radius: 0; height: 100px;position: relative;padding: 10px; margin-bottom: 0; }
#nv_portal .vw .d table {margin: 0;}
</style>
<div id="ct" class="ct2 wp cl">
<div class="mn">
<article class="vw">
<div class="h hm bm" style="margin-top: 0;">
<h1 class="ph" id="article_title">systemctl 命令完全指南 </h1>
<div class="ph" id="article_copyright">
<span>作者： 
    	 
    		    			<span class="textcut"><a href="http://www.tecmint.com/manage-services-using-systemd-and-systemctl-in-linux/" target="_blank">Avishek Kumar</a></span>
    		    	    	<span>译者： 
<a href="https://linux.cn/lctt/" target=_blank>LCTT</a>&nbsp;<a href="/lctt/GOLinux" target="_blank">joeren</a></span>
<p id="article_date">
| 2015-07-31 08:00&nbsp;&nbsp;
评论: <a href="portal.php?mod=comment&id=5926&idtype=aid" title="查看全部评论"><em id="_commentnum">18</em></a>&nbsp;收藏: <em id="_favtimes">30</em>&nbsp;分享: <em id="_sharetimes">2</em>&nbsp;&nbsp;&nbsp;&nbsp;
</p>
</div>
</div>

<div class="d" style="width: 100%;margin: 0;">
<div id="article_content" style="border-radius:0;">
<p>Systemctl是一个systemd工具，主要负责控制systemd系统和服务管理器。</p>
<p>Systemd是一个系统管理守护进程、工具和库的集合，用于取代System V初始进程。Systemd的功能是用于集中管理和配置类UNIX系统。</p>
<p>在Linux生态系统中，Systemd被部署到了大多数的标准Linux发行版中，只有为数不多的几个发行版尚未部署。Systemd通常是所有其它守护进程的父进程，但并非总是如此。</p>
<p><img src="https://img.linux.net.cn/data/attachment/album/201507/30/210221zg6czg8yogegegay.jpg" alt="Manage Linux Services Using Systemctl" /></p>
<p><em>使用Systemctl管理Linux服务</em></p>
<p>本文旨在阐明在运行systemd的系统上&ldquo;如何控制系统和服务&rdquo;。</p>
<h3 id="toc_1">Systemd初体验和Systemctl基础</h3>
<h4 id="toc_2">1. 首先检查你的系统中是否安装有systemd并确定当前安装的版本</h4>
<pre class="prettyprint linenums"><code># systemctl --version

systemd 215
+PAM +AUDIT +SELINUX +IMA +SYSVINIT +LIBCRYPTSETUP +GCRYPT +ACL +XZ -SECCOMP -APPARMOR
</code></pre>
<p>上例中很清楚地表明，我们安装了215版本的systemd。</p>
<h4 id="toc_3">2. 检查systemd和systemctl的二进制文件和库文件的安装位置</h4>
<pre class="prettyprint linenums"><code># whereis systemd 
systemd: /usr/lib/systemd /etc/systemd /usr/share/systemd /usr/share/man/man1/systemd.1.gz


# whereis systemctl
systemctl: /usr/bin/systemctl /usr/share/man/man1/systemctl.1.gz
</code></pre>
<h4 id="toc_4">3. 检查systemd是否运行</h4>
<pre class="prettyprint linenums"><code># ps -eaf | grep [s]ystemd

root         1     0  0 16:27 ?        00:00:00 /usr/lib/systemd/systemd --switched-root --system --deserialize 23
root       444     1  0 16:27 ?        00:00:00 /usr/lib/systemd/systemd-journald
root       469     1  0 16:27 ?        00:00:00 /usr/lib/systemd/systemd-udevd
root       555     1  0 16:27 ?        00:00:00 /usr/lib/systemd/systemd-logind
dbus       556     1  0 16:27 ?        00:00:00 /bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation
</code></pre>
<p><strong>注意</strong>：systemd是作为父进程（PID=1）运行的。在上面带（-e）参数的ps命令输出中，选择所有进程，（-a）选择除会话前导外的所有进程，并使用（-f）参数输出完整格式列表（即 -eaf）。</p>
<p>也请注意上例中后随的方括号和例子中剩余部分。方括号表达式是grep的字符类表达式的一部分。</p>
<h4 id="toc_5">4. 分析systemd启动进程</h4>
<pre class="prettyprint linenums"><code># systemd-analyze
Startup finished in 487ms (kernel) + 2.776s (initrd) + 20.229s (userspace) = 23.493s
</code></pre>
<h4 id="toc_6">5. 分析启动时各个进程花费的时间</h4>
<pre class="prettyprint linenums"><code># systemd-analyze blame

8.565s mariadb.service
7.991s webmin.service
6.095s postfix.service
4.311s httpd.service
3.926s firewalld.service
3.780s kdump.service
3.238s tuned.service
1.712s network.service
1.394s lvm2-monitor.service
1.126s systemd-logind.service
....
</code></pre>
<h4 id="toc_7">6. 分析启动时的关键链</h4>
<pre class="prettyprint linenums"><code># systemd-analyze critical-chain

The time after the unit is active or started is printed after the "@" character.
The time the unit takes to start is printed after the "+" character.

multi-user.target @20.222s
└─mariadb.service @11.657s +8.565s
  └─network.target @11.168s
    └─network.service @9.456s +1.712s
      └─NetworkManager.service @8.858s +596ms
        └─firewalld.service @4.931s +3.926s
          └─basic.target @4.916s
            └─sockets.target @4.916s
              └─dbus.socket @4.916s
                └─sysinit.target @4.905s
                  └─systemd-update-utmp.service @4.864s +39ms
                    └─auditd.service @4.563s +301ms
                      └─systemd-tmpfiles-setup.service @4.485s +69ms
                        └─rhel-import-state.service @4.342s +142ms
                          └─local-fs.target @4.324s
                            └─boot.mount @4.286s +31ms
                              └─systemd-fsck@dev-disk-by\x2duuid-79f594ad\x2da332\x2d4730\x2dbb5f\x2d85d19608096
                                └─dev-disk-by\x2duuid-79f594ad\x2da332\x2d4730\x2dbb5f\x2d85d196080964.device @4
</code></pre>
<p><strong>重要</strong>：Systemctl接受服务（.service），挂载点（.mount），套接口（.socket）和设备（.device）作为单元。</p>
<h4 id="toc_8">7. 列出所有可用单元</h4>
<pre class="prettyprint linenums"><code># systemctl list-unit-files

UNIT FILE                                   STATE   
proc-sys-fs-binfmt_misc.automount           static  
dev-hugepages.mount                         static  
dev-mqueue.mount                            static  
proc-sys-fs-binfmt_misc.mount               static  
sys-fs-fuse-connections.mount               static  
sys-kernel-config.mount                     static  
sys-kernel-debug.mount                      static  
tmp.mount                                   disabled
brandbot.path                               disabled
.....
</code></pre>
<h4 id="toc_9">8. 列出所有运行中单元</h4>
<pre class="prettyprint linenums"><code># systemctl list-units

UNIT                                        LOAD   ACTIVE SUB       DESCRIPTION
proc-sys-fs-binfmt_misc.automount           loaded active waiting   Arbitrary Executable File Formats File Syste
sys-devices-pc...0-1:0:0:0-block-sr0.device loaded active plugged   VBOX_CD-ROM
sys-devices-pc...:00:03.0-net-enp0s3.device loaded active plugged   PRO/1000 MT Desktop Adapter
sys-devices-pc...00:05.0-sound-card0.device loaded active plugged   82801AA AC'97 Audio Controller
sys-devices-pc...:0:0-block-sda-sda1.device loaded active plugged   VBOX_HARDDISK
sys-devices-pc...:0:0-block-sda-sda2.device loaded active plugged   LVM PV Qzyo3l-qYaL-uRUa-Cjuk-pljo-qKtX-VgBQ8
sys-devices-pc...0-2:0:0:0-block-sda.device loaded active plugged   VBOX_HARDDISK
sys-devices-pl...erial8250-tty-ttyS0.device loaded active plugged   /sys/devices/platform/serial8250/tty/ttyS0
sys-devices-pl...erial8250-tty-ttyS1.device loaded active plugged   /sys/devices/platform/serial8250/tty/ttyS1
sys-devices-pl...erial8250-tty-ttyS2.device loaded active plugged   /sys/devices/platform/serial8250/tty/ttyS2
sys-devices-pl...erial8250-tty-ttyS3.device loaded active plugged   /sys/devices/platform/serial8250/tty/ttyS3
sys-devices-virtual-block-dm\x2d0.device    loaded active plugged   /sys/devices/virtual/block/dm-0
sys-devices-virtual-block-dm\x2d1.device    loaded active plugged   /sys/devices/virtual/block/dm-1
sys-module-configfs.device                  loaded active plugged   /sys/module/configfs
...
</code></pre>
<h4 id="toc_10">9. 列出所有失败单元</h4>
<pre class="prettyprint linenums"><code># systemctl --failed

UNIT          LOAD   ACTIVE SUB    DESCRIPTION
kdump.service loaded failed failed Crash recovery kernel arming

LOAD   = Reflects whether the unit definition was properly loaded.
ACTIVE = The high-level unit activation state, i.e. generalization of SUB.
SUB    = The low-level unit activation state, values depend on unit type.

1 loaded units listed. Pass --all to see loaded but inactive units, too.
To show all installed unit files use 'systemctl list-unit-files'.
</code></pre>
<h4 id="toc_11">10. 检查某个单元（如 cron.service）是否启用</h4>
<pre class="prettyprint linenums"><code># systemctl is-enabled crond.service

enabled
</code></pre>
<h4 id="toc_12">11. 检查某个单元或服务是否运行</h4>
<pre class="prettyprint linenums"><code># systemctl status firewalld.service

firewalld.service - firewalld - dynamic firewall daemon
   Loaded: loaded (/usr/lib/systemd/system/firewalld.service; enabled)
   Active: active (running) since Tue 2015-04-28 16:27:55 IST; 34min ago
 Main PID: 549 (firewalld)
   CGroup: /system.slice/firewalld.service
           └─549 /usr/bin/python -Es /usr/sbin/firewalld --nofork --nopid

Apr 28 16:27:51 tecmint systemd[1]: Starting firewalld - dynamic firewall daemon...
Apr 28 16:27:55 tecmint systemd[1]: Started firewalld - dynamic firewall daemon.
</code></pre>
<h3 id="toc_13">使用Systemctl控制并管理服务</h3>
<h4 id="toc_14">12. 列出所有服务（包括启用的和禁用的）</h4>
<pre class="prettyprint linenums"><code># systemctl list-unit-files --type=service

UNIT FILE                                   STATE   
arp-ethers.service                          disabled
auditd.service                              enabled 
autovt@.service                             disabled
blk-availability.service                    disabled
brandbot.service                            static  
collectd.service                            disabled
console-getty.service                       disabled
console-shell.service                       disabled
cpupower.service                            disabled
crond.service                               enabled 
dbus-org.fedoraproject.FirewallD1.service   enabled 
....
</code></pre>
<h4 id="toc_15">13. Linux中如何启动、重启、停止、重载服务以及检查服务（如 httpd.service）状态</h4>
<pre class="prettyprint linenums"><code># systemctl start httpd.service
# systemctl restart httpd.service
# systemctl stop httpd.service
# systemctl reload httpd.service
# systemctl status httpd.service

httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; enabled)
   Active: active (running) since Tue 2015-04-28 17:21:30 IST; 6s ago
  Process: 2876 ExecStop=/bin/kill -WINCH ${MAINPID} (code=exited, status=0/SUCCESS)
 Main PID: 2881 (httpd)
   Status: "Processing requests..."
   CGroup: /system.slice/httpd.service
           ├─2881 /usr/sbin/httpd -DFOREGROUND
           ├─2884 /usr/sbin/httpd -DFOREGROUND
           ├─2885 /usr/sbin/httpd -DFOREGROUND
           ├─2886 /usr/sbin/httpd -DFOREGROUND
           ├─2887 /usr/sbin/httpd -DFOREGROUND
           └─2888 /usr/sbin/httpd -DFOREGROUND

Apr 28 17:21:30 tecmint systemd[1]: Starting The Apache HTTP Server...
Apr 28 17:21:30 tecmint httpd[2881]: AH00558: httpd: Could not reliably determine the server's fully q...ssage
Apr 28 17:21:30 tecmint systemd[1]: Started The Apache HTTP Server.
Hint: Some lines were ellipsized, use -l to show in full.
</code></pre>
<p><strong>注意</strong>：当我们使用systemctl的start，restart，stop和reload命令时，我们不会从终端获取到任何输出内容，只有status命令可以打印输出。</p>
<h4 id="toc_16">14. 如何激活服务并在启动时启用或禁用服务（即系统启动时自动启动服务）</h4>
<pre class="prettyprint linenums"><code># systemctl is-active httpd.service
# systemctl enable httpd.service
# systemctl disable httpd.service
</code></pre>
<h4 id="toc_17">15. 如何屏蔽（让它不能启动）或显示服务（如 httpd.service）</h4>
<pre class="prettyprint linenums"><code># systemctl mask httpd.service
ln -s '/dev/null' '/etc/systemd/system/httpd.service'

# systemctl unmask httpd.service
rm '/etc/systemd/system/httpd.service'
</code></pre>
<h4 id="toc_18">16. 使用systemctl命令杀死服务</h4>
<pre class="prettyprint linenums"><code># systemctl kill httpd
# systemctl status httpd

httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; enabled)
   Active: failed (Result: exit-code) since Tue 2015-04-28 18:01:42 IST; 28min ago
 Main PID: 2881 (code=exited, status=0/SUCCESS)
   Status: "Total requests: 0; Current requests/sec: 0; Current traffic:   0 B/sec"

Apr 28 17:37:29 tecmint systemd[1]: httpd.service: Got notification message from PID 2881, but recepti...bled.
Apr 28 17:37:29 tecmint systemd[1]: httpd.service: Got notification message from PID 2881, but recepti...bled.
Apr 28 17:37:39 tecmint systemd[1]: httpd.service: Got notification message from PID 2881, but recepti...bled.
Apr 28 17:37:39 tecmint systemd[1]: httpd.service: Got notification message from PID 2881, but recepti...bled.
Apr 28 17:37:49 tecmint systemd[1]: httpd.service: Got notification message from PID 2881, but recepti...bled.
Apr 28 17:37:49 tecmint systemd[1]: httpd.service: Got notification message from PID 2881, but recepti...bled.
Apr 28 17:37:59 tecmint systemd[1]: httpd.service: Got notification message from PID 2881, but recepti...bled.
Apr 28 17:37:59 tecmint systemd[1]: httpd.service: Got notification message from PID 2881, but recepti...bled.
Apr 28 18:01:42 tecmint systemd[1]: httpd.service: control process exited, code=exited status=226
Apr 28 18:01:42 tecmint systemd[1]: Unit httpd.service entered failed state.
Hint: Some lines were ellipsized, use -l to show in full.
</code></pre>
<h3 id="toc_19">使用Systemctl控制并管理挂载点</h3>
<h4 id="toc_20">17. 列出所有系统挂载点</h4>
<pre class="prettyprint linenums"><code># systemctl list-unit-files --type=mount

UNIT FILE                     STATE   
dev-hugepages.mount           static  
dev-mqueue.mount              static  
proc-sys-fs-binfmt_misc.mount static  
sys-fs-fuse-connections.mount static  
sys-kernel-config.mount       static  
sys-kernel-debug.mount        static  
tmp.mount                     disabled
</code></pre>
<h4 id="toc_21">18. 挂载、卸载、重新挂载、重载系统挂载点并检查系统中挂载点状态</h4>
<pre class="prettyprint linenums"><code># systemctl start tmp.mount
# systemctl stop tmp.mount
# systemctl restart tmp.mount
# systemctl reload tmp.mount
# systemctl status tmp.mount

tmp.mount - Temporary Directory
   Loaded: loaded (/usr/lib/systemd/system/tmp.mount; disabled)
   Active: active (mounted) since Tue 2015-04-28 17:46:06 IST; 2min 48s ago
    Where: /tmp
     What: tmpfs
     Docs: man:hier(7)

http://www.freedesktop.org/wiki/Software/systemd/APIFileSystems

  Process: 3908 ExecMount=/bin/mount tmpfs /tmp -t tmpfs -o mode=1777,strictatime (code=exited, status=0/SUCCESS)

Apr 28 17:46:06 tecmint systemd[1]: Mounting Temporary Directory...
Apr 28 17:46:06 tecmint systemd[1]: tmp.mount: Directory /tmp to mount over is not empty, mounting anyway.
Apr 28 17:46:06 tecmint systemd[1]: Mounted Temporary Directory.
</code></pre>
<h4 id="toc_22">19. 在启动时激活、启用或禁用挂载点（系统启动时自动挂载）</h4>
<pre class="prettyprint linenums"><code># systemctl is-active tmp.mount
# systemctl enable tmp.mount
# systemctl disable  tmp.mount
</code></pre>
<h4 id="toc_23">20. 在Linux中屏蔽（让它不能启用）或可见挂载点</h4>
<pre class="prettyprint linenums"><code># systemctl mask tmp.mount

ln -s '/dev/null' '/etc/systemd/system/tmp.mount'

# systemctl unmask tmp.mount

rm '/etc/systemd/system/tmp.mount'
</code></pre>
<h3 id="toc_24">使用Systemctl控制并管理套接口</h3>
<h4 id="toc_25">21. 列出所有可用系统套接口</h4>
<pre class="prettyprint linenums"><code># systemctl list-unit-files --type=socket

UNIT FILE                    STATE   
dbus.socket                  static  
dm-event.socket              enabled 
lvm2-lvmetad.socket          enabled 
rsyncd.socket                disabled
sshd.socket                  disabled
syslog.socket                static  
systemd-initctl.socket       static  
systemd-journald.socket      static  
systemd-shutdownd.socket     static  
systemd-udevd-control.socket static  
systemd-udevd-kernel.socket  static  

11 unit files listed.
</code></pre>
<h4 id="toc_26">22. 在Linux中启动、重启、停止、重载套接口并检查其状态</h4>
<pre class="prettyprint linenums"><code># systemctl start cups.socket
# systemctl restart cups.socket
# systemctl stop cups.socket
# systemctl reload cups.socket
# systemctl status cups.socket

cups.socket - CUPS Printing Service Sockets
   Loaded: loaded (/usr/lib/systemd/system/cups.socket; enabled)
   Active: active (listening) since Tue 2015-04-28 18:10:59 IST; 8s ago
   Listen: /var/run/cups/cups.sock (Stream)

Apr 28 18:10:59 tecmint systemd[1]: Starting CUPS Printing Service Sockets.
Apr 28 18:10:59 tecmint systemd[1]: Listening on CUPS Printing Service Sockets.
</code></pre>
<h4 id="toc_27">23. 在启动时激活套接口，并启用或禁用它（系统启动时自启动）</h4>
<pre class="prettyprint linenums"><code># systemctl is-active cups.socket
# systemctl enable cups.socket
# systemctl disable cups.socket
</code></pre>
<h4 id="toc_28">24. 屏蔽（使它不能启动）或显示套接口</h4>
<pre class="prettyprint linenums"><code># systemctl mask cups.socket
ln -s '/dev/null' '/etc/systemd/system/cups.socket'

# systemctl unmask cups.socket
rm '/etc/systemd/system/cups.socket'
</code></pre>
<h3 id="toc_29">服务的CPU利用率（分配额）</h3>
<h4 id="toc_30">25. 获取当前某个服务的CPU分配额（如httpd）</h4>
<pre class="prettyprint linenums"><code># systemctl show -p CPUShares httpd.service

CPUShares=1024
</code></pre>
<p><strong>注意</strong>：各个服务的默认CPU分配份额=1024，你可以增加/减少某个进程的CPU分配份额。</p>
<h4 id="toc_31">26. 将某个服务（httpd.service）的CPU分配份额限制为2000 CPUShares/</h4>
<pre class="prettyprint linenums"><code># systemctl set-property httpd.service CPUShares=2000
# systemctl show -p CPUShares httpd.service

CPUShares=2000
</code></pre>
<p><strong>注意</strong>：当你为某个服务设置CPUShares，会自动创建一个以服务名命名的目录（如 httpd.service），里面包含了一个名为90-CPUShares.conf的文件，该文件含有CPUShare限制信息，你可以通过以下方式查看该文件：</p>
<pre class="prettyprint linenums"><code># vi /etc/systemd/system/httpd.service.d/90-CPUShares.conf 

[Service]
CPUShares=2000        
</code></pre>
<h4 id="toc_32">27. 检查某个服务的所有配置细节</h4>
<pre class="prettyprint linenums"><code># systemctl show httpd

Id=httpd.service
Names=httpd.service
Requires=basic.target
Wants=system.slice
WantedBy=multi-user.target
Conflicts=shutdown.target
Before=shutdown.target multi-user.target
After=network.target remote-fs.target nss-lookup.target systemd-journald.socket basic.target system.slice
Description=The Apache HTTP Server
LoadState=loaded
ActiveState=active
SubState=running
FragmentPath=/usr/lib/systemd/system/httpd.service
....
</code></pre>
<h4 id="toc_33">28. 分析某个服务（httpd）的关键链</h4>
<pre class="prettyprint linenums"><code># systemd-analyze critical-chain httpd.service

The time after the unit is active or started is printed after the "@" character.
The time the unit takes to start is printed after the "+" character.

httpd.service +142ms
└─network.target @11.168s
  └─network.service @9.456s +1.712s
    └─NetworkManager.service @8.858s +596ms
      └─firewalld.service @4.931s +3.926s
        └─basic.target @4.916s
          └─sockets.target @4.916s
            └─dbus.socket @4.916s
              └─sysinit.target @4.905s
                └─systemd-update-utmp.service @4.864s +39ms
                  └─auditd.service @4.563s +301ms
                    └─systemd-tmpfiles-setup.service @4.485s +69ms
                      └─rhel-import-state.service @4.342s +142ms
                        └─local-fs.target @4.324s
                          └─boot.mount @4.286s +31ms
                            └─systemd-fsck@dev-disk-by\x2duuid-79f594ad\x2da332\x2d4730\x2dbb5f\x2d85d196080964.service @4.092s +149ms
                              └─dev-disk-by\x2duuid-79f594ad\x2da332\x2d4730\x2dbb5f\x2d85d196080964.device @4.092s
</code></pre>
<h4 id="toc_34">29. 获取某个服务（httpd）的依赖性列表</h4>
<pre class="prettyprint linenums"><code># systemctl list-dependencies httpd.service

httpd.service
├─system.slice
└─basic.target
  ├─firewalld.service
  ├─microcode.service
  ├─rhel-autorelabel-mark.service
  ├─rhel-autorelabel.service
  ├─rhel-configure.service
  ├─rhel-dmesg.service
  ├─rhel-loadmodules.service
  ├─paths.target
  ├─slices.target
  │ ├─-.slice
  │ └─system.slice
  ├─sockets.target
  │ ├─dbus.socket
....
</code></pre>
<h4 id="toc_35">30. 按等级列出控制组</h4>
<pre class="prettyprint linenums"><code># systemd-cgls

├─1 /usr/lib/systemd/systemd --switched-root --system --deserialize 23
├─user.slice
│ └─user-0.slice
│   └─session-1.scope
│     ├─2498 sshd: root@pts/0    
│     ├─2500 -bash
│     ├─4521 systemd-cgls
│     └─4522 systemd-cgls
└─system.slice
  ├─httpd.service
  │ ├─4440 /usr/sbin/httpd -DFOREGROUND
  │ ├─4442 /usr/sbin/httpd -DFOREGROUND
  │ ├─4443 /usr/sbin/httpd -DFOREGROUND
  │ ├─4444 /usr/sbin/httpd -DFOREGROUND
  │ ├─4445 /usr/sbin/httpd -DFOREGROUND
  │ └─4446 /usr/sbin/httpd -DFOREGROUND
  ├─polkit.service
  │ └─721 /usr/lib/polkit-1/polkitd --no-debug
....
</code></pre>
<h4 id="toc_36">31. 按CPU、内存、输入和输出列出控制组</h4>
<pre class="prettyprint linenums"><code># systemd-cgtop

Path                                                              Tasks   %CPU   Memory  Input/s Output/s

/                                                                    83    1.0   437.8M        -        -
/system.slice                                                         -    0.1        -        -        -
/system.slice/mariadb.service                                         2    0.1        -        -        -
/system.slice/tuned.service                                           1    0.0        -        -        -
/system.slice/httpd.service                                           6    0.0        -        -        -
/system.slice/NetworkManager.service                                  1      -        -        -        -
/system.slice/atop.service                                            1      -        -        -        -
/system.slice/atopacct.service                                        1      -        -        -        -
/system.slice/auditd.service                                          1      -        -        -        -
/system.slice/crond.service                                           1      -        -        -        -
/system.slice/dbus.service                                            1      -        -        -        -
/system.slice/firewalld.service                                       1      -        -        -        -
/system.slice/lvm2-lvmetad.service                                    1      -        -        -        -
/system.slice/polkit.service                                          1      -        -        -        -
/system.slice/postfix.service                                         3      -        -        -        -
/system.slice/rsyslog.service                                         1      -        -        -        -
/system.slice/system-getty.slice/getty@tty1.service                   1      -        -        -        -
/system.slice/systemd-journald.service                                1      -        -        -        -
/system.slice/systemd-logind.service                                  1      -        -        -        -
/system.slice/systemd-udevd.service                                   1      -        -        -        -
/system.slice/webmin.service                                          1      -        -        -        -
/user.slice/user-0.slice/session-1.scope                              3      -        -        -        -
</code></pre>
<h3 id="toc_37">控制系统运行等级</h3>
<h4 id="toc_38">32. 启动系统救援模式</h4>
<pre class="prettyprint linenums"><code># systemctl rescue

Broadcast message from root@tecmint on pts/0 (Wed 2015-04-29 11:31:18 IST):

The system is going down to rescue mode NOW!
</code></pre>
<h4 id="toc_39">33. 进入紧急模式</h4>
<pre class="prettyprint linenums"><code># systemctl emergency

Welcome to emergency mode! After logging in, type "journalctl -xb" to view
system logs, "systemctl reboot" to reboot, "systemctl default" to try again
to boot into default mode.
</code></pre>
<h4 id="toc_40">34. 列出当前使用的运行等级</h4>
<pre class="prettyprint linenums"><code># systemctl get-default

multi-user.target
</code></pre>
<h4 id="toc_41">35. 启动运行等级5，即图形模式</h4>
<pre class="prettyprint linenums"><code># systemctl isolate runlevel5.target
或
# systemctl isolate graphical.target
</code></pre>
<h4 id="toc_42">36. 启动运行等级3，即多用户模式（命令行）</h4>
<pre class="prettyprint linenums"><code># systemctl isolate runlevel3.target
或
# systemctl isolate multiuser.target
</code></pre>
<h4 id="toc_43">36. 设置多用户模式或图形模式为默认运行等级</h4>
<pre class="prettyprint linenums"><code># systemctl set-default runlevel3.target

# systemctl set-default runlevel5.target
</code></pre>
<h4 id="toc_44">37. 重启、停止、挂起、休眠系统或使系统进入混合睡眠</h4>
<pre class="prettyprint linenums"><code># systemctl reboot

# systemctl halt

# systemctl suspend

# systemctl hibernate

# systemctl hybrid-sleep
</code></pre>
<p>对于不知运行等级为何物的人，说明如下。</p>
<ul>
<li>Runlevel 0 : 关闭系统</li>
<li>Runlevel 1 : 救援？维护模式</li>
<li>Runlevel 3 : 多用户，无图形系统</li>
<li>Runlevel 4 : 多用户，无图形系统</li>
<li>Runlevel 5 : 多用户，图形化系统</li>
<li>Runlevel 6 : 关闭并重启机器</li>
</ul>
<p>到此为止吧。保持连线，进行评论。别忘了在下面的评论中为我们提供一些有价值的反馈哦。喜欢我们、与我们分享，求扩散。</p>
<hr />
<p>via: <a href="http://www.tecmint.com/manage-services-using-systemd-and-systemctl-in-linux/">http://www.tecmint.com/manage-services-using-systemd-and-systemctl-in-linux/</a></p>
<p>作者：<a href="http://www.tecmint.com/author/avishek/">Avishek Kumar</a> 译者：<a href="https://github.com/GOLinux">GOLinux</a> 校对：<a href="https://github.com/wxy">wxy</a></p>
<p>本文由 <a href="https://github.com/LCTT/TranslateProject">LCTT</a> 原创翻译，<a href="https://linux.cn/">Linux中国</a> 荣誉推出</p>  					<section><img style="width:24px;height: 24px;float: right;" src="https://img.linux.net.cn/static/image/common/linisi.svg"><br class="clear"></section>
</div>
</div>
<br class="clear" />
<div class="vw">
<div id="add_comment" class="h bm" style="display: none;">
<div class="bm_h cl">
<h3>发表评论</h3>
</div>
<div class="bm_c pbn">
<form id="cform" name="cform" action="portal.php?mod=portalcp&ac=comment" method="post" autocomplete="off">
<div class="tedt">
<div class="area">
<textarea name="message" rows="10" class="pt" id="message" onkeydown="ctrlEnter(event, 'commentsubmit_btn');"></textarea>
</div>
</div>

<div class="mtm z"><span id="seccode_cSY38Z64"></span>		
<script type="text/javascript" reload="1">updateseccode('cSY38Z64', '<sec> <span id="sec<hash>" onclick="showMenu(this.id);"><sec></span><div id="sec<hash>_menu" class="p_pop p_opt" style="display:none"><sec></div>', 'portal::view');</script>
<script type="text/javascript">
(function($){
$("#cform").submit(function(e) {
if ($("#checksec_none_cSY38Z64").length>0) {
alert("请输入验证码");
return false;
} else if ($("#checksec_error_cSY38Z64").length>0) {
alert("验证码输入错误，请重新输入");
return false;
} else if ($("#checksec_loading_cSY38Z64").length>0) {
alert("验证码验证中……");
return false;
}
});
})(jQuery);
</script>
</div>
<input type="hidden" name="portal_referer" value="https://linux.cn/article-5926-1.html#comment">
<input type="hidden" name="referer" value="https://linux.cn/article-5926-1.html#comment" />
<input type="hidden" name="id" value="0" />
<input type="hidden" name="idtype" value="" />
<input type="hidden" name="aid" value="5926">
<input id="reppid" type="hidden" name="reppid" value="">
<input type="hidden" name="formhash" value="7ba44b27">
<input type="hidden" name="replysubmit" value="true">
<input type="hidden" name="commentsubmit" value="true" />
<p class="mtm" style="text-align: center;"><button type="submit" name="commentsubmit_btn" id="commentsubmit_btn" value="true" class="pn"><strong>评论</strong></button></p>
<br class="clear" />
</form>
</div>
</div>
<div id="comment" class="bm h">
<div class="bm_h cl">
<h3 class="z"><a name="comment"></a>最新评论</h3>
</div>
<div id="comment_ul" class="bm_c">
<div style="text-align: center;"><button type="button" class="pnc" style="font-size: 24px;width: 160px;" id="c_add" onclick="showWindow(this.id, 'portal.php?mod=portalcp&ac=comment&op=new&aid=5926', 'get', 0);"><strong>发表评论</strong></button></div><a name="comment_anchor_48735"></a>
<dl id="comment_48735_li" class="pbm bbda cl">
<dt class="mbm  ">
<span class=" xw0 vm">来自浙江杭州的 Chrome 69.0|Windows 7 用户</span>
<span class=" xw0 vm">2020-08-24 11:27</span>
<span class="y xw0 xi2 opt" style="margin-right: 5px;">
<a class="replyadd" href="portal.php?mod=review&amp;action=postreview&amp;do=support&amp;idtype=aid&amp;tid=5926&amp;pid=48735&amp;hash=7ba44b27" onclick="ajaxmenu(this, 3000, 0, 0, '43', '');return false;"><span id="review_support_48735">1</span> 赞</a> 
<!--<a href="javascript:;" onclick="portal_comment_reppost(48735, '5926');">回复</a> --><a id="reply_48735" onclick="showWindow('comment', this.href, 'get', 0);" href="portal.php?mod=portalcp&amp;ac=comment&amp;op=reply&amp;cid=48735&amp;aid=5926&amp;idtype=">回复</a> </span>	
</dt>
<dd>
学习了，很详细</dd>
</dl><a name="comment_anchor_48652"></a>
<dl id="comment_48652_li" class="pbm bbda cl">
<dt class="mbm  ">
<span class=" xw0 vm">来自江西赣州的 Chrome 81.0|Windows 10 用户</span>
<span class=" xw0 vm">2020-07-22 15:31</span>
<span class="y xw0 xi2 opt" style="margin-right: 5px;">
<a class="replyadd" href="portal.php?mod=review&amp;action=postreview&amp;do=support&amp;idtype=aid&amp;tid=5926&amp;pid=48652&amp;hash=7ba44b27" onclick="ajaxmenu(this, 3000, 0, 0, '43', '');return false;"><span id="review_support_48652">1</span> 赞</a> 
<!--<a href="javascript:;" onclick="portal_comment_reppost(48652, '5926');">回复</a> --><a id="reply_48652" onclick="showWindow('comment', this.href, 'get', 0);" href="portal.php?mod=portalcp&amp;ac=comment&amp;op=reply&amp;cid=48652&amp;aid=5926&amp;idtype=">回复</a> </span>	
</dt>
<dd>
66666</dd>
</dl><a name="comment_anchor_48562"></a>
<dl id="comment_48562_li" class="pbm bbda cl">
<dt class="mbm  ">
<span class=" xw0 vm">来自四川成都的 Chrome 39.0|Windows 10 用户</span>
<span class=" xw0 vm">2020-06-24 15:49</span>
<span class="y xw0 xi2 opt" style="margin-right: 5px;">
<a class="replyadd" href="portal.php?mod=review&amp;action=postreview&amp;do=support&amp;idtype=aid&amp;tid=5926&amp;pid=48562&amp;hash=7ba44b27" onclick="ajaxmenu(this, 3000, 0, 0, '43', '');return false;"><span id="review_support_48562">1</span> 赞</a> 
<!--<a href="javascript:;" onclick="portal_comment_reppost(48562, '5926');">回复</a> --><a id="reply_48562" onclick="showWindow('comment', this.href, 'get', 0);" href="portal.php?mod=portalcp&amp;ac=comment&amp;op=reply&amp;cid=48562&amp;aid=5926&amp;idtype=">回复</a> </span>	
</dt>
<dd>
14、19、23中的 systemctl is-active 并不是用于激活，而是查询运行状态。和 systemctl enable、systemctl disable 配对的应该是 systemctl is-enabled</dd>
</dl><a name="comment_anchor_47451"></a>
<dl id="comment_47451_li" class="pbm bbda cl">
<dt class="mbm  s1">
<span class=" xw0 vm">来自上海的 Chrome 74.0|Windows 10 用户</span>
<span class=" xw0 vm">2019-06-08 06:14</span>
<span class="y xw0 xi2 opt" style="margin-right: 5px;">
<a class="replyadd" href="portal.php?mod=review&amp;action=postreview&amp;do=support&amp;idtype=aid&amp;tid=5926&amp;pid=47451&amp;hash=7ba44b27" onclick="ajaxmenu(this, 3000, 0, 0, '43', '');return false;"><span id="review_support_47451">2</span> 赞</a> 
<!--<a href="javascript:;" onclick="portal_comment_reppost(47451, '5926');">回复</a> --><a id="reply_47451" onclick="showWindow('comment', this.href, 'get', 0);" href="portal.php?mod=portalcp&amp;ac=comment&amp;op=reply&amp;cid=47451&amp;aid=5926&amp;idtype=">回复</a> </span>	
</dt>
<dd>
17. 列出所有系统挂载点<br />
<br />
tmp.mount&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;disabled<br />
<br />
<br />
tmp.mount&nbsp;&nbsp;是什么东西？怎么得来的？</dd>
</dl><a name="comment_anchor_47450"></a>
<dl id="comment_47450_li" class="pbm bbda cl">
<dt class="mbm  s1">
<span class=" xw0 vm">来自上海的 Chrome 74.0|Windows 10 用户</span>
<span class=" xw0 vm">2019-06-08 06:12</span>
<span class="y xw0 xi2 opt" style="margin-right: 5px;">
<a class="replyadd" href="portal.php?mod=review&amp;action=postreview&amp;do=support&amp;idtype=aid&amp;tid=5926&amp;pid=47450&amp;hash=7ba44b27" onclick="ajaxmenu(this, 3000, 0, 0, '43', '');return false;"><span id="review_support_47450">2</span> 赞</a> 
<!--<a href="javascript:;" onclick="portal_comment_reppost(47450, '5926');">回复</a> --><a id="reply_47450" onclick="showWindow('comment', this.href, 'get', 0);" href="portal.php?mod=portalcp&amp;ac=comment&amp;op=reply&amp;cid=47450&amp;aid=5926&amp;idtype=">回复</a> </span>	
</dt>
<dd>
17. 列出所有系统挂载点<br />
<br />
tmp.mount&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;disabled<br />
<br />
tmp.mount&nbsp;&nbsp;是什么东西？怎么得来的？</dd>
</dl><a name="comment_anchor_47449"></a>
<dl id="comment_47449_li" class="pbm bbda cl">
<dt class="mbm  s1">
<span class=" xw0 vm">来自上海的 Chrome 74.0|Windows 10 用户</span>
<span class=" xw0 vm">2019-06-08 06:12</span>
<span class="y xw0 xi2 opt" style="margin-right: 5px;">
<a class="replyadd" href="portal.php?mod=review&amp;action=postreview&amp;do=support&amp;idtype=aid&amp;tid=5926&amp;pid=47449&amp;hash=7ba44b27" onclick="ajaxmenu(this, 3000, 0, 0, '43', '');return false;"><span id="review_support_47449">2</span> 赞</a> 
<!--<a href="javascript:;" onclick="portal_comment_reppost(47449, '5926');">回复</a> --><a id="reply_47449" onclick="showWindow('comment', this.href, 'get', 0);" href="portal.php?mod=portalcp&amp;ac=comment&amp;op=reply&amp;cid=47449&amp;aid=5926&amp;idtype=">回复</a> </span>	
</dt>
<dd>
17. 列出所有系统挂载点<br />
<br />
tmp.mount&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;disabled<br />
<br />
tmp.mount&nbsp;&nbsp;是什么东西？怎么得来的？</dd>
</dl><a name="comment_anchor_47448"></a>
<dl id="comment_47448_li" class="pbm bbda cl">
<dt class="mbm  s1">
<span class=" xw0 vm">来自上海的 Chrome 74.0|Windows 10 用户</span>
<span class=" xw0 vm">2019-06-08 06:12</span>
<span class="y xw0 xi2 opt" style="margin-right: 5px;">
<a class="replyadd" href="portal.php?mod=review&amp;action=postreview&amp;do=support&amp;idtype=aid&amp;tid=5926&amp;pid=47448&amp;hash=7ba44b27" onclick="ajaxmenu(this, 3000, 0, 0, '43', '');return false;"><span id="review_support_47448">2</span> 赞</a> 
<!--<a href="javascript:;" onclick="portal_comment_reppost(47448, '5926');">回复</a> --><a id="reply_47448" onclick="showWindow('comment', this.href, 'get', 0);" href="portal.php?mod=portalcp&amp;ac=comment&amp;op=reply&amp;cid=47448&amp;aid=5926&amp;idtype=">回复</a> </span>	
</dt>
<dd>
17. 列出所有系统挂载点<br />
<br />
tmp.mount&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;disabled<br />
<br />
tmp.mount&nbsp;&nbsp;是什么东西？怎么得来的？</dd>
</dl><a name="comment_anchor_47447"></a>
<dl id="comment_47447_li" class="pbm bbda cl">
<dt class="mbm  s1">
<span class=" xw0 vm">来自上海的 Chrome 74.0|Windows 10 用户</span>
<span class=" xw0 vm">2019-06-08 06:12</span>
<span class="y xw0 xi2 opt" style="margin-right: 5px;">
<a class="replyadd" href="portal.php?mod=review&amp;action=postreview&amp;do=support&amp;idtype=aid&amp;tid=5926&amp;pid=47447&amp;hash=7ba44b27" onclick="ajaxmenu(this, 3000, 0, 0, '43', '');return false;"><span id="review_support_47447">2</span> 赞</a> 
<!--<a href="javascript:;" onclick="portal_comment_reppost(47447, '5926');">回复</a> --><a id="reply_47447" onclick="showWindow('comment', this.href, 'get', 0);" href="portal.php?mod=portalcp&amp;ac=comment&amp;op=reply&amp;cid=47447&amp;aid=5926&amp;idtype=">回复</a> </span>	
</dt>
<dd>
17. 列出所有系统挂载点<br />
<br />
tmp.mount&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;disabled<br />
<br />
tmp.mount&nbsp;&nbsp;是什么东西？怎么得来的？</dd>
</dl><a name="comment_anchor_46031"></a>
<dl id="comment_46031_li" class="pbm bbda cl">
<dt class="mbm user s1">
<a href="space/48369/" class="xi2 xw1 vm" c="1" target="_blank">amwuje [Microsoft Edge 14.14393|Windows 10]</a>
<span class=" xw0 vm">2017-07-04 14:47</span>
<span class="y xw0 xi2 opt" style="margin-right: 5px;">
<a class="replyadd" href="portal.php?mod=review&amp;action=postreview&amp;do=support&amp;idtype=aid&amp;tid=5926&amp;pid=46031&amp;hash=7ba44b27" onclick="ajaxmenu(this, 3000, 0, 0, '43', '');return false;"><span id="review_support_46031">3</span> 赞</a> 
<!--<a href="javascript:;" onclick="portal_comment_reppost(46031, '5926');">回复</a> --><a id="reply_46031" onclick="showWindow('comment', this.href, 'get', 0);" href="portal.php?mod=portalcp&amp;ac=comment&amp;op=reply&amp;cid=46031&amp;aid=5926&amp;idtype=">回复</a> </span>	
</dt>
<dd>
感谢，学到了很多！</dd>
</dl><a name="comment_anchor_45844"></a>
<dl id="comment_45844_li" class="pbm bbda cl">
<dt class="mbm  s2">
<span class=" xw0 vm">来自四川成都的 Firefox 54.0|Windows 7 用户</span>
<span class=" xw0 vm">2017-06-15 12:29</span>
<span class="y xw0 xi2 opt" style="margin-right: 5px;">
<a class="replyadd" href="portal.php?mod=review&amp;action=postreview&amp;do=support&amp;idtype=aid&amp;tid=5926&amp;pid=45844&amp;hash=7ba44b27" onclick="ajaxmenu(this, 3000, 0, 0, '43', '');return false;"><span id="review_support_45844">4</span> 赞</a> 
<!--<a href="javascript:;" onclick="portal_comment_reppost(45844, '5926');">回复</a> --><a id="reply_45844" onclick="showWindow('comment', this.href, 'get', 0);" href="portal.php?mod=portalcp&amp;ac=comment&amp;op=reply&amp;cid=45844&amp;aid=5926&amp;idtype=">回复</a> </span>	
</dt>
<dd>
感谢楼主分享！</dd>
</dl><a name="comment_anchor_44009"></a>
<dl id="comment_44009_li" class="pbm bbda cl">
<dt class="mbm  s1">
<span class=" xw0 vm">来自陕西西安的 Chrome 55.0|Windows 7 用户</span>
<span class=" xw0 vm">2017-01-11 11:17</span>
<span class="y xw0 xi2 opt" style="margin-right: 5px;">
<a class="replyadd" href="portal.php?mod=review&amp;action=postreview&amp;do=support&amp;idtype=aid&amp;tid=5926&amp;pid=44009&amp;hash=7ba44b27" onclick="ajaxmenu(this, 3000, 0, 0, '43', '');return false;"><span id="review_support_44009">3</span> 赞</a> 
<!--<a href="javascript:;" onclick="portal_comment_reppost(44009, '5926');">回复</a> --><a id="reply_44009" onclick="showWindow('comment', this.href, 'get', 0);" href="portal.php?mod=portalcp&amp;ac=comment&amp;op=reply&amp;cid=44009&amp;aid=5926&amp;idtype=">回复</a> </span>	
</dt>
<dd>
感谢楼主分享！</dd>
</dl><a name="comment_anchor_43497"></a>
<dl id="comment_43497_li" class="pbm bbda cl">
<dt class="mbm  s2">
<span class=" xw0 vm">来自美国的 Chrome 54.0|Windows 7 用户</span>
<span class=" xw0 vm">2016-12-07 17:08</span>
<span class="y xw0 xi2 opt" style="margin-right: 5px;">
<a class="replyadd" href="portal.php?mod=review&amp;action=postreview&amp;do=support&amp;idtype=aid&amp;tid=5926&amp;pid=43497&amp;hash=7ba44b27" onclick="ajaxmenu(this, 3000, 0, 0, '43', '');return false;"><span id="review_support_43497">6</span> 赞</a> 
<!--<a href="javascript:;" onclick="portal_comment_reppost(43497, '5926');">回复</a> --><a id="reply_43497" onclick="showWindow('comment', this.href, 'get', 0);" href="portal.php?mod=portalcp&amp;ac=comment&amp;op=reply&amp;cid=43497&amp;aid=5926&amp;idtype=">回复</a> </span>	
</dt>
<dd>
希望增加 控制reboot时启动顺序等相关说明 谢谢！</dd>
</dl><a name="comment_anchor_34310"></a>
<dl id="comment_34310_li" class="pbm bbda cl">
<dd class="list"><blockquote id="replist_34310_34301" class="replist"  ><dt class="mbm s2"><span class="info">
<div class="z count">[1] </div>来自陕西西安的 Chrome 43.0|Windows 8.1 用户 发表于 2015-08-04 17:56 的评论：
</span>
<div id="opt_34310_34301" class="y opt"><a href="portal.php?mod=review&amp;action=postreview&amp;do=support&amp;idtype=aid&amp;tid=5926&amp;pid=34301&amp;hash=7ba44b27" onclick="ajaxmenu(this, 3000, 0, 0, '43', '');return false;"><span name="review_support_rep_34301">5</span> 赞</a> <a id="reply_34301" href="portal.php?mod=portalcp&amp;ac=comment&amp;op=reply&amp;cid=34301&amp;aid=5926&amp;idtype=" onclick="showWindow('comment', this.href, 'get', 0);">回复</a>   </div></dt>
<div class="msg">第一条命令应该是 systemctl --version 吧</div>
</blockquote></dd>
<dt class="mbm user s2">
<a href="space/1/" class="xi2 xw1 vm" c="1" target="_blank">linux [Chrome 44.0|Mac 10.10]</a>
<span class=" xw0 vm">2015-08-04 20:33</span>
<span class="y xw0 xi2 opt" style="margin-right: 5px;">
<a class="replyadd" href="portal.php?mod=review&amp;action=postreview&amp;do=support&amp;idtype=aid&amp;tid=5926&amp;pid=34310&amp;hash=7ba44b27" onclick="ajaxmenu(this, 3000, 0, 0, '43', '');return false;"><span id="review_support_34310">4</span> 赞</a> 
<!--<a href="javascript:;" onclick="portal_comment_reppost(34310, '5926');">回复</a> --><a id="reply_34310" onclick="showWindow('comment', this.href, 'get', 0);" href="portal.php?mod=portalcp&amp;ac=comment&amp;op=reply&amp;cid=34310&amp;aid=5926&amp;idtype=">回复</a> </span>	
</dt>
<dd>
您说的对，已经修改。</dd>
</dl><a name="comment_anchor_34306"></a>
<dl id="comment_34306_li" class="pbm bbda cl">
<dd class="list"><blockquote id="replist_34306_34262" class="replist"  ><blockquote id="replist_34306_34238" class="replist"  ><dt class="mbm s3"><span class="info">
<div class="z count">[1] </div><a href="space/20893/" class="xi2 xw1" c="1" target="_blank">XYJK1002 [Chrome 42.0|Windows 7]</a> 发表于 2015-07-31 08:24 的评论：
</span>
<div id="opt_34306_34238" class="y opt"><a href="portal.php?mod=review&amp;action=postreview&amp;do=support&amp;idtype=aid&amp;tid=5926&amp;pid=34238&amp;hash=7ba44b27" onclick="ajaxmenu(this, 3000, 0, 0, '43', '');return false;"><span name="review_support_rep_34238">12</span> 赞</a> <a id="reply_34238" href="portal.php?mod=portalcp&amp;ac=comment&amp;op=reply&amp;cid=34238&amp;aid=5926&amp;idtype=" onclick="showWindow('comment', this.href, 'get', 0);">回复</a>   </div></dt>
<div class="msg">Linux中国出品，必属精品。</div>
</blockquote><dt class="mbm s1"><span class="info">
<div class="z count">[2] </div><a href="space/1/" class="xi2 xw1" c="1" target="_blank">linux [Chrome 43.0|Mac 10.10]</a> 发表于 2015-08-01 21:26 的评论：
</span>
<div id="opt_34306_34262" class="y opt"><a href="portal.php?mod=review&amp;action=postreview&amp;do=support&amp;idtype=aid&amp;tid=5926&amp;pid=34262&amp;hash=7ba44b27" onclick="ajaxmenu(this, 3000, 0, 0, '43', '');return false;"><span name="review_support_rep_34262">3</span> 赞</a> <a id="reply_34262" href="portal.php?mod=portalcp&amp;ac=comment&amp;op=reply&amp;cid=34262&amp;aid=5926&amp;idtype=" onclick="showWindow('comment', this.href, 'get', 0);">回复</a>   </div></dt>
<div class="msg">哇！太赞誉了，感谢本文译者 GOLinux ！欢迎更多的兄弟姐妹加入LCTT ： http://lctt.github.io/ ~</div>
</blockquote></dd>
<dt class="mbm user s2">
<a href="space/15563/" class="xi2 xw1 vm" c="1" target="_blank">夜域诡士 [Chrome 31.0|Windows 7]</a>
<span class=" xw0 vm">2015-08-04 18:36</span>
<span class="y xw0 xi2 opt" style="margin-right: 5px;">
<a class="replyadd" href="portal.php?mod=review&amp;action=postreview&amp;do=support&amp;idtype=aid&amp;tid=5926&amp;pid=34306&amp;hash=7ba44b27" onclick="ajaxmenu(this, 3000, 0, 0, '43', '');return false;"><span id="review_support_34306">6</span> 赞</a> 
<!--<a href="javascript:;" onclick="portal_comment_reppost(34306, '5926');">回复</a> --><a id="reply_34306" onclick="showWindow('comment', this.href, 'get', 0);" href="portal.php?mod=portalcp&amp;ac=comment&amp;op=reply&amp;cid=34306&amp;aid=5926&amp;idtype=">回复</a> </span>	
</dt>
<dd>
Linux中国出品，必属精品。</dd>
</dl><a name="comment_anchor_34263"></a>
<dl id="comment_34263_li" class="pbm bbda cl">
<dt class="mbm user s2">
<a href="space/6599/" class="xi2 xw1 vm" c="1" target="_blank">netb2c [Chrome 44.0|Fedora]</a>
<span class=" xw0 vm">2015-08-01 22:08</span>
<span class="y xw0 xi2 opt" style="margin-right: 5px;">
<a class="replyadd" href="portal.php?mod=review&amp;action=postreview&amp;do=support&amp;idtype=aid&amp;tid=5926&amp;pid=34263&amp;hash=7ba44b27" onclick="ajaxmenu(this, 3000, 0, 0, '43', '');return false;"><span id="review_support_34263">6</span> 赞</a> 
<!--<a href="javascript:;" onclick="portal_comment_reppost(34263, '5926');">回复</a> --><a id="reply_34263" onclick="showWindow('comment', this.href, 'get', 0);" href="portal.php?mod=portalcp&amp;ac=comment&amp;op=reply&amp;cid=34263&amp;aid=5926&amp;idtype=">回复</a> </span>	
</dt>
<dd>
谢谢分享，谢谢LC！</dd>
</dl><div class="ptm pbm cl">
</div>
</div>
</div>
</div>
<div class="h bm_c bm z" id="footer_info">
<p class="copyright">
    	 
    		    			    			<span class="z textcut">译自：<a href="http://www.tecmint.com/manage-services-using-systemd-and-systemctl-in-linux/" target="_blank">tecmint.com</a></span>
    			    		    		<span class="y">作者： Avishek Kumar</span>    		<br class="clear" />
    	    	<span class="z">原创：<a href="https://linux.cn/lctt/" target=_blank>LCTT</a> <a href="https://linux.cn/article-5926-1.html" target="_blank">https://linux.cn/article-5926-1.html</a></span>
            			<span class="y">译者： joeren</span>    		<br class="clear" />
    	    	<br />
    	    		<span>本文由 LCTT 原创翻译，<a href="https://linux.cn/article-5926-1.html">Linux中国首发</a>。也想加入译者行列，为开源做一些自己的贡献么？欢迎加入 <a href="http://lctt.github.io/" target=_blank>LCTT</a>！<br />翻译工作和译文发表仅用于学习和交流目的，翻译工作遵照 <a href="http://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh" target=_blank>CC-BY-NC-SA 协议规定</a>，如果我们的工作有侵犯到您的权益，请及时联系我们。</span>
    		    		<br class="clear" />
    		<span style="color:red;">欢迎遵照 <a href="http://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh" target=_blank>CC-BY-NC-SA 协议规定</a>转载，敬请在正文中标注并保留原文/译文链接和作者/译者等信息。</span>
                		<br class="clear" />
    	    	<span>文章仅代表作者的知识和看法，如有不同观点，请楼下排队<a href="javascript:void(0);" onclick="$('message').focus();">吐槽</a> :D</span>
    	<br class="clear" />
</p>



<div class="o cl ptm pbm">
<a href="home.php?mod=spacecp&amp;ac=favorite&amp;type=article&amp;id=5926&amp;handlekey=favoritearticlehk_5926" id="a_favorite" onclick="showWindow(this.id, this.href, 'get', 0);" class="favorite z" title="收藏"></a>
<!-- <a href="misc.php?mod=invite&amp;action=article&amp;id=5926" id="a_invite" onclick="showWindow('invite', this.href, 'get', 0);" class="invite z" title="邀请"></a> -->
<a href="https://linux.cn/article-5926-1.html?pr" class="print z" title="打印"></a>
				
</div>
<div class="pren pbm cl">
<em>上一篇：<a href="https://linux.cn/article-5920-1.html">如何向 Linux 内核提交驱动</a></em><em>下一篇：<a href="https://linux.cn/article-5930-1.html">使用Hexo在Github上搭建自己的博客</a></em></div>
</div>
<div ><div id="translator_info" class="bm" style="position: relative;margin: 8px 4px 8px 0 !important;float: right;">
<div class="bm_h cl">
LCTT 译者
</div>
<div class="bm_c">
<div >
<a href="/lctt/GOLinux" target="_blank"><img class="avatar" src="https://avatars.githubusercontent.com/u/7578603?" style="max-width: 64px; float: left;margin-top: 10px;" /></a>
<div style="float: left;margin-left: 10px;font-size: 12px;line-height: 1.5em; ">
<div>
<a href="https://github.com/GOLinux" target="_blank"><img src="https://img.linux.net.cn/static/image/common/github_icon.png" style="vertical-align:middle;" /></a> <a href="/lctt/GOLinux" target="_blank" style="font-weight: bold;">joeren</a> 💎</div>
<div class="addfiles">共计翻译： <span class="num" style="color: #f00;font-weight: 700;">157.0</span> 篇
| 共计贡献： <span class="num" style="color: #f00;font-weight: 700;">1039</span> 天</div>
<div>贡献时间：2014-05-15 -&gt; 2017-03-19</div><a href="/lctt/GOLinux" target="_blank">访问我的 LCTT 主页</a> | <a href="https://github.com/GOLinux" target="_blank">在 GitHub 上关注我</a>
</div>
<br class="clear" />
</div>
</div>
</div>
</div>

<div id="related" class="bm block z">
<div class="bm_h cl">
<h3>相关阅读</h3>
</div>
</div>
<br class="clear" />
</article>
</div>

</div>


<input type="hidden" id="portalview" value="1">

<script type="text/javascript">
(function($){
$(window).load(function() {

// 文章内插图及注释

var max_width = $("#article_content").width() - 60;
var imgp = $("#article_content IMG").parents("P");
imgp.each(function(){
$(this).addClass("article_img");
var img = $(this).find("IMG");
if (img.parent("A").is("A")) {
img.unwrap();
}
// 如果有图片描述
var desc = null;
if ((desc = $(this).next("P")) && desc && desc.contents() && desc.contents().first().is("EM") ) {
desc.addClass("article_img_desc");
desc_txt = desc.contents().first().text();
img.attr({"title":desc_txt,"alt":desc_txt});
} else if ((desc = img.next("BR").next("EM")) && desc.text()) {
var desc_txt = desc.text();
img.next("BR").remove();
img.next("EM").remove();
$(this).after("<p class='article_img_desc'><em>" + desc_txt + "</em></p>");
} else {
var desc_txt = img.attr("alt") || img.attr("title");
if (desc_txt != '' && typeof desc_txt != 'undefined') {
$(this).after("<p class='article_img_desc'><em>" + desc_txt + "</em></p>");
}
}
if (img.attr("width") > max_width) {
img.attr("width",'');
img.attr("height",'');
img.css("cursor","pointer");
img.click(function(){window.open(img.attr("src"));});
} else if (img.width() > max_width) {
img.css("height",parseInt(img.height() * (max_width / img.attr("width"))));
img.css("width",max_width);
img.css("cursor","pointer");
img.click(function(){window.open(img.attr("src"));});
}
});

var pre = $("#article_content PRE");
pre.each(function(){
// 如果有代码描述
var desc = null;
if ((desc = $(this).next("P")) && desc && desc.contents() && desc.contents().first().is("EM") ) {
desc.addClass("article_img_desc");
desc_txt = desc.contents().first().text();
}
});

// 链接
var re_sitelink = /^https?:\/\/(www.)?linux(.net)?.cn\//i;
$("#article_content a").map(function(){
if ($(this).attr('href') == undefined) {
$(this).css({'visibility':'hidden'});
} else if ($(this).attr('href').substr(0,1) == '#') {
$(this).attr('href','https://linux.cn/article-5926-1.html' + $(this).attr('href'));
}
if (re_sitelink.test($(this).attr('href'))) {
if ($(this).text() == 'Linux中国') $(this).attr('href',$(location).attr('href'));
} else {
$(this).addClass("ext").attr({"rel":"external nofollow","target":"_blank"});
}
});

// 视频
$("video").map(function() {
width = $(this).attr("width");
height = $(this).attr("height");
$(this).wrap("<div class='videoContainer'></div>").parent()
.css({width: width,height : height});
});
$("#article_content table").map(function() {
var page_width = parseInt($("#article_content").css('width')) - 30;
var width = parseInt($(this).css('width')) + 2;
if (width > page_width) {
width = page_width;
width = width + "px";
$(this).wrap("<section class='bm'><section style='white-space:nowrap;overflow:scroll;'></section></section>")
.parent().parent().css('width',width).prepend("<section class='hm bm_h'>&lt; 如显示不全，请左右滑动 &gt;</section>")
.append("<section class='hm bm_f'></section>");
}
});
$("#article_content table td").map(function() {
var c = $(this).text();
if (c.length > 20) $(this).css("white-space","normal");

});
})
})(jQuery);
</script>
<link rel="stylesheet" href="https://img.linux.net.cn/static/js/prettify/prettify.css?yX7" type="text/css" />
<script src="https://img.linux.net.cn/static/js/prettify/prettify.min.js?yX7" type="text/javascript"></script>
<script type="text/javascript">
var sourceBaseUrl = "https://img.linux.net.cn/static/js/tinymce/plugins/prettify";
prettyPrint();
</script>
<script type="text/javascript">
var getblock_last = 0;
var related = [];	
(function($){
$(window).scroll(function() {
var load_more_bottom = $('#article_content').offset().top + $('#article_content').height();
var scrollPos = $(window).scrollTop() + jQuery(window).height();
var last = Date.parse(new Date())
if (scrollPos - load_more_bottom > 300 && last - getblock_last > 1000) {
getblock_last = last
}
});
})(jQuery);

</script>	</div>
    <div id="footer">
        <p>
            <span>Linux.CN &copy; 2003 →→→  Linux中国</span>
            <span class="line">|</span>
            <span>Powered by <strong>DX</strong> | 图片存储于<a href="http://www.qiniu.com/" target="_blank">七牛云</a></span>
        </p>
        <p>
            <a href="http://www.miitbeian.gov.cn/" target="_blank">京ICP备05083684号-1</a>            京公网安备110105001595
        </p>
        <p>
        <a href="https://linux.cn/legal.html">服务条款</a> |
        除特别申明外，本站原创内容版权遵循 <a href="http://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh" target="_blank">CC-BY-NC-SA 协议规定</a></p>
        <p>
        <a href="https://linux.cn/"><img src="https://img.linux.net.cn/static/image/common/linuxcn_logo_mini.png" align="absmiddle" /></a>
        <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank"><img src="https://img.linux.net.cn/static/image/common/cc.png" align="absmiddle" /></a>
        </p>
<p>
<a href="forum.php?mod=misc&action=showdarkroom" >小黑屋</a><span class="pipe">|</span></p>
</div>

<div id="ft" class="cl"></div>
<script src="home.php?mod=misc&ac=sendmail&rand=1611300254" type="text/javascript"></script>
<div id="scrolltop">
<span>
<a href="javascript:void();" class="wxicon" onmouseover="show_qrcode(event,'#qrcode', SITEURL + 'article-5926-1.html?utm_source=weixin');" onmouseout="show_qrcode(event,'#qrcode','');"></a>
<a title="分享到微博" href="javascript:void( share_tsina(SITEURL + 'article-5926-1.html?utm_source=weibo','article_title','article_content','https://img.linux.net.cn/data/attachment/album/201507/30/210221zg6czg8yogegegay.jpg') );" class="tsina"></a>
<a title="收藏" href="home.php?mod=spacecp&amp;ac=favorite&amp;type=article&amp;id=5926&amp;handlekey=favoritearticlehk_5926" id="a_favorite" onclick="showWindow(this.id, this.href, 'get', 0);" class="favorite" title="收藏"></a>
    	<a href="article-5926-1.html?pr" class="print" title="!print!"></a>

</span>
<span hidefocus="true"><a title="返回顶部" onclick="window.scrollTo('0','0')" class="scrolltopa" ><b>返回顶部</b></a></span>
</div>
<script type="text/javascript">_attachEvent(window, 'scroll', function () { showTopLink(); });</script>
<div id="qrcode">
<p>分享到微信</p>
<div id="canvas"></div>
<p><em>打开微信，点击顶部的“╋”，<br />
使用“扫一扫”将网页分享至微信。</em></p></div>
<!-- script type="text/javascript" src="https://img.linux.net.cn/static/js/ads.js?yX7"></script -->
<!-- div id="LyX7CisOsS" style="display: none; background-color: #A00; position: fixed; top: 0; width: 100%; z-index: 9999; left: 0; font-size: 16px; color: #fff; text-align: center; padding: 10px; opacity: 0.8;">请将我们加入您的广告过滤器的白名单，请支持开源站点。谢谢您。</div -->
<script type="text/javascript">
(function($){
$(window).load(function() {
/*if ($('#pleaseRemoveOurSiteFromBlackList').length == 0 && $(window).width() >= 480) {
$('#LyX7CisOsS').css('display','block');
}*/
if (location.href.substr(0,17) != 'https://linux.cn/') {
location.href = 'https://linux.cn/';
}
function roundTopFocus() {
if ($('.topfocus').length) {
//var tf1 = $('.topfocus').children().first();
//$('.topfocus').children().fadeOut('fast',function(){tf1.remove().appendTo($('.topfocus')).fadeIn()}).fadeIn();
} else if ($('.article_titlead').length) {
var ad1 = $('.article_titlead').children().first();
$('.article_titlead').children().fadeOut('slow',function(){ad1.remove().appendTo($('.article_titlead')).fadeIn()}).fadeIn();

}
}
setInterval(roundTopFocus, 10000);
});
})(jQuery);
</script>
</body>
</html>
