https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-8.0.20-1.el7.x86_64.rpm-bundle.tar

	
solved:

https://pkgs.org/search/?q=libcrypto.so.1.1

1,修改密码，mysql8初始对密码要求高，简单的字符串不让改。先改成:MyNewPass@123;

alter user 'root'@'localhost' identified by 'MyNewPass@123';

2,第二部:输入:show variables like 'validate_password%';貌似没有改密码不让你看。

3，

validate_password.check_user_name :用户名检测，默认关闭

validate_password.dictionary_file :字典文件，就是要在字典规则里才能满足密码的条件。

validate_password.length   :密码的长度至少为8位

validate_password.mixed_case_count   ：密码中至少有一个大写小字母

validate_password.number_count ：密码中至少一个数字

validate_password.special_char_count  :密码中至少一个特殊字符

validate_password.policy :密码的安全策略

你只需要把用户检测关闭，然后安全策略改成LOW,密码长度改成你想要的位数。

set global validate_password.check_user_name=OFF;

set global validate_password.plicy=LOW;

set global validate_password.length=4;

最后修改为简单密码:

 ALTER user 'root'@'localhost' identified by 'root';
