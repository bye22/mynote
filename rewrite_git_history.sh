#git filter-branch --index-filter 'git rm --cached --ignore-unmatch '
#d8072fce827295d8d4c42cdccecf3629344c56b2 system-OS/linux/blackarch/blackTools.md
#159dc9c5f9902f48f3ad1506fd5961ce306debd7 blob/doc/NovaStudio用户手册-V3.3.pdf
#36bf02d7ff14ba82926c837ff6c18272a2da90a3 blob/wordpress.org/wordpress-5.4.1.tar.gz
#2f7663eaf44195144f6dc43b0f0b206a22d8cc4e blob/wordpress.org/wordpress-5.4.1.zip
#3d389f24eb209b78c0d9d0b77cc028403a2da211 dev/database/mysql/MySQL数据库开发的三十六条军规_石展_完整.pdf
#72c11f7979fcf44eefd97e8ea899a20dfac3545e system/linux/blackarch/blackarch-guide-zh.pdf
#de78aaa24aa160196c98a38687b253e281a2b340 vim/jdt-language-server-latest.tar.gz
#0d9ed6296758df486f4bf870230e150ce862e06b wordpress-5.3.tar.gz
#0a8d0dbf7a1cf6efd57063710c2a766dfdceea74 auto-office/docx/docx01.docx
#bded1eb35a46fcf52585192817b1eaa72c84b5bd 123620kszymmm5sjfdwwk4.jpg
#git filter-branch --index-filter "git rm --cached --ignore-unmatch 'blob/doc/NovaStudio用户手册-V3.3.pdf'"
git filter-branch --index-filter "git rm --cached --ignore-unmatch 'blob/wordpress.org/wordpress-5.4.1.tar.gz'"
sh git_del_history.sh
git filter-branch --index-filter "git rm --cached --ignore-unmatch 'blob/wordpress.org/wordpress-5.4.1.zip'"
sh git_del_history.sh
git filter-branch --index-filter "git rm --cached --ignore-unmatch 'dev/database/mysql/MySQL数据库开发的三十六条军规_石展_完整.pdf'"
sh git_del_history.sh
git filter-branch --index-filter "git rm --cached --ignore-unmatch 'system/linux/blackarch/blackarch-guide-zh.pdf'"
sh git_del_history.sh
git filter-branch --index-filter "git rm --cached --ignore-unmatch 'vim/jdt-language-server-latest.tar.gz'"
sh git_del_history.sh
git filter-branch --index-filter "git rm --cached --ignore-unmatch 'wordpress-5.3.tar.gz'"
sh git_del_history.sh
git filter-branch --index-filter "git rm --cached --ignore-unmatch 'auto-office/docx/docx01.docx'"
sh git_del_history.sh
git filter-branch --index-filter "git rm --cached --ignore-unmatch '123620kszymmm5sjfdwwk4.jpg'"
sh git_del_history.sh
