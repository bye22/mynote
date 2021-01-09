git filter-branch --index-filter "git rm --cached --ignore-unmatch 'blob/wordpress.org/wordpress-5.4.1.tar.gz'"
sh git_del_history.sh
