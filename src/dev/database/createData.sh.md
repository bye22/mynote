```sh
#!/bin/bash
#
#Author: 脚本小王子
#Date: 2021-06-08
#Description: 快速创建多个表及测试数据
#Usage: 请查看--help
source /etc/profile
source ~/.bash_profile 
 
 
############################################################# 功能函数 Begin ##################################################################
​
        #显示消息
        #showType='errSysMsg/errSys/errUserMsg/warning/msg/msg2/OK'
        #错误输出（以红色字体输出） errSysMsg：捕捉系统错误后发现相信并退出；errSys：捕捉到系统错误后退出；errUserMsg：自定义错误并退出，但不退出（errSysMsg及errUserMsg可以赋第三个参数isExit为非1来控制不退出）
        #警告（以黄色字体输出）  warning：显示warning，但不退出
        #显示信息（以白色字体输出，OK以绿色输出） msg：输出信息并换行；msg2：输出信息不换行；OK：输出绿色OK并换行
        function showMsg()
        {
                errState=${PIPESTATUS[0]}
                #errState="$?"
                #showMsgTestMode=1      #如果设为1，则把有exit 1均改为return 0，便于调试其中函数
                local showType="$1"
                local showContent="$2"
                local isExit="$3"
                #如果isExit为空，则默认出错时该退出
                if [ "${isExit}" = "" ]; then
                        isExit=1
                fi
                isShowRelation=`echo "${pid}" | sed "s/-->/\n0x01_Flag/g" | grep "0x01_Flag" | wc -l`
                showType=`echo ${showType} | tr 'A-Z' 'a-z'`
                case "${showType}" in
                        errsysmsg)
                                if [ "${errState}" -ne 0 ]; then
                                        echo -e "\033[31;49;1m[`date +%F' '%T`] Error: ${showContent}\033[39;49;0m" | tee -a ${logFile} >&2
                                        if [ "${isShowRelation}" -gt 1 ]; then  # 调用层次超过1次时才显示调用关系
                                                echo -e "\033[31;49;1m[`date +%F' '%T`] Call Relation: bash${pid}\033[39;49;0m" | tee -a ${logFile} >&2
                                        fi
                                        if [ "${isExit}" -eq 1 ]; then
                                                if [ "${showMsgTestMode}" = "1" ]; then
                                                        return 1
                                                else 
                                                        exit 1
                                                fi
                                        fi
                                fi
                        ;;
                        errsys)
                                if [ "$errState" -ne 0 ]; then
                                        if [ "${isExit}" -eq 1 ]; then
                                                if [ "${showMsgTestMode}" = "1" ]; then
                                                        return 1
                                                else 
                                                        exit 1
                                                fi
                                        fi
                                fi
                        ;;
                        errusermsg)
                                echo -e "\033[31;49;1m[`date +%F' '%T`] Error: ${showContent}\033[39;49;0m"  | tee -a ${logFile} >&2
                                if [ "${isShowRelation}" -gt 1 ]; then  # 调用层次超过1次时才显示调用关系
                                        echo -e "\033[31;49;1m[`date +%F' '%T`] Call Relation: bash${pid}\033[39;49;0m" | tee -a ${logFile} >&2
                                fi
                                if [ "${isExit}" -eq 1 ]; then
                                        if [ "${isExit}" -eq 1 ]; then
                                                if [ "${showMsgTestMode}" = "1" ]; then
                                                        return 1
                                                else 
                                                        exit 1
                                                fi
                                        fi
                                fi
                        ;;
                        warning)
                                echo -e "\033[33;49;1m[`date +%F' '%T`] Warnning: ${showContent}\033[39;49;0m"  | tee -a ${logFile}
                                if [ "${isShowRelation}" -gt 1 ]; then  # 调用层次超过1次时才显示调用关系
                                        echo -e "\033[33;49;1m[`date +%F' '%T`] Call Relation: bash${pid}\033[39;49;0m"  | tee -a ${logFile}
                                fi
                        ;;
                        warning2)
                                echo -e "\033[33;49;1mWarnning: ${showContent}\033[39;49;0m"  | tee -a ${logFile}
                        ;;
                        msg)
                                echo "[`date +%F' '%T`] ${showContent}" | tee -a ${logFile}
                        ;;
                        msg2)
                                echo -n "[`date +%F' '%T`] ${showContent}" | tee -a ${logFile}
                        ;;
                        ok)
                                echo "OK" >> ${logFile}
                                echo -e "\033[32;49;1mOK\033[39;49;0m" 
                        ;;
                        *)
                                echo -e "\033[31;49;1m[`date +%F' '%T`] Error: Call founction showMsg error\033[39;49;0m"  | tee -a ${logFile}
                                        if [ "${isExit}" -eq 1 ]; then
                                                if [ "${showMsgTestMode}" = "1" ]; then
                                                        return 1
                                                else 
                                                        exit 1
                                                fi
                                        fi
                        ;;
                esac
        }
        #showMsgTestMode=1; logFile=/tmp/test.log
 
        #执行sql语句
        # executeSql "select now()" 
        function executeSql()
        {
                local sql="$1"
                if [ -z "$mysqlUser" -o "$mysqlUser" = "" -o -z "${mysqlPwd}" -o "${mysqlPwd}" = "" ]; then
                        showMsg "errUserMsg" "mysql user or mysql password is not vaild."
                fi
                if [ "$sql" = "" ]
                then
                        showMsg "errUserMsg" "sql statement is null "
                else
                        echo -e "$sql" | mysql --defaults-extra-file=${my_cnf}  $useDBName --default-character-set=utf8 -N 
                fi
        }
 
        #创建mycnf文件，供executeSql使用
        function createMycnfFile()
        {
                mysqlHost="$1"
                mysqlPort="$2"
                mysqlUser="$3"
                mysqlPwd="$4"
                #isIP=`echo "${mysqlHost}" | grep -E '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$' | wc -l`
                if [ "${mysqlHost}" = 'localhost' ]; then
 
                        mysqlPid=`netstat -naltp | grep 'LISTEN' | awk   '$4~/'"$mysqlPort"'/{print $0}' | awk '{print $NF}' | awk -F'/' '{print $1}'`
                        mysqlSock=`netstat -nap | grep -w "${mysqlPid}/mysqld" | grep 'LISTENING' | grep -v 'mysqlx.sock' | awk '{print $NF}'`
                        echo -e "\n[client]\nhost=${mysqlHost}\nuser=${mysqlUser}\npassword='${mysqlPwd}'\nsocket=${mysqlSock}" > ${my_cnf}
                        echo -e "\n[mysqldump]\nhost=${mysqlHost}\nuser=${mysqlUser}\npassword='${mysqlPwd}'\nsocket=${mysqlSock}" >> ${my_cnf}
                else
                        echo -e "\n[client]\nhost=${mysqlHost}\nport=${mysqlPort}\nuser=${mysqlUser}\npassword='${mysqlPwd}'" > ${my_cnf}
                        echo -e "\n[mysqldump]\nhost=${mysqlHost}\nport=${mysqlPort}\nuser=${mysqlUser}\npassword='${mysqlPwd}'" >> ${my_cnf}
                fi
 
        }
############################################################# 功能函数 End ####################################################################
 
function shellInit()
{
        sid=`basename $0`
        export pid="${pid}-->$sid"
        theFiledir=`echo $(cd "$(dirname "$0")"; pwd)`
        cd ${theFiledir}
        #默认日志文件为“本文件名.log”，如main函数有传入logFile参数（如不带路径则为当前目录），则以传入的日志文件名为准
        theFileName=`basename $0 | awk -F"." '{print $1}'`
        if [ "${logFile}" = "" ]; then
                logFile="${theFileName}.log"
        fi
        logFilePath=`dirname ${logFile}`
        if [ "${logFilePath}" = '.' ]; then
                logFilePath=${theFiledir}
        fi
        logFileName=`basename ${logFile}`
        logFile="${logFilePath}/${logFileName}"
        mkdir -p ${logFilePath}
        touch ${logFile}
        shellPId="$$"
        my_cnf="/tmp/.my_${shellPId}.cnf"
        tmpFile="/tmp/.tmpFile.${shellPId}"
        tmpFile2="/tmp/.tmpFile2.${shellPId}"
        #退出/中止（包括导常退出）脚本时执行的命令
        trapCmd="rm -f /tmp/.my_${shellPId}.cnf"
        trapCmd="${trapCmd}; rm -f /tmp/.tmpFile.${shellPId}"
        trapCmd="${trapCmd}; rm -f /tmp/.tmpFile2.${shellPId}"
        trap 'eval ${trapCmd}' exit
        #输出执行方法
        showMsg 'msg'
        showMsg 'msg' "Run Shell: ${cmdShell} ${parameterString}"
        #--------以上为框架规定，建议不要做修改----------
        #执行Mysql的初始参数
        if [ "${mysqlHost}" = "" ]; then
                mysqlHost='localhost'
        fi
        createMycnfFile "${mysqlHost}" "${mysqlPort}" "${mysqlUser}" "${mysqlPwd}"
        ########################
        #执行Oracle的初始参数
        #oraUser=scott
        #oraPwd=tiger
}
 
function check()
{
        isRunBatchNum=`echo "${runBatch}" | grep -E -w '^[0-9]+$' | wc -l`
        if [ "${isRunBatchNum}" != "1" ]; then
                showMsg 'errUserMsg' "\${runBatch} only a number"
        fi
        executeSql "select 1" > /dev/null
        showMsg 'errSysMsg' "Can not connet to the MySQL(mysqlHost=${mysqlHost},mysqlPort=${mysqlPort},mysqlUser=${mysqlUser},DBName=${useDBName})"
}
 
 
# 创建一张表并插入测试数据
# 如果要修改表结构则修改此函数
function createOneTableTestData()
{
        local tableName="$1"
        local runBatch="$2"
        sql="
          create database if not exists ${useDBName};
          # 建测试表
          CREATE TABLE ${tableName} (
            id int NOT NULL AUTO_INCREMENT PRIMARY KEY comment '自增主键', 
            dept tinyint not null comment '部门id',
            name varchar(30) comment '用户名称',
            create_time datetime not null comment '注册时间', 
            last_login_time datetime comment '最后登录时间'
          ) comment '测试表';
          #手工插入第一条测试数据，后面根据此行数据作为基础进行插入
          insert into ${tableName} values(1,1,'user_1', now(), now());
        "
        showMsg 'msg2' "Create table ${useDBName}.${tableName}......"
        executeSql "${sql}"
        showMsg 'errSysMsg' "Some error occur when execute '${sql}'"
        showMsg 'OK'
 
        sql="set @i = 1;"
        # 循环拼接SQL
        for i in $(seq 1 ${runBatch}); do
          sql="${sql}
            insert into ${tableName}(id, dept, name, create_time, last_login_time) 
            select @i:=@i+1,
              left(rand()*10,1) as dept,
              concat('user_',@i), 
              date_add(create_time,interval + (${runBatch}-@i) * cast(rand()*10 as signed) SECOND),
              date_add(date_add(create_time,interval + (${runBatch} - @i) *cast(rand()*10 as signed) SECOND), interval + cast(rand()*1000000 as signed) SECOND) 
            from ${tableName};
            "
        done
        showMsg 'msg2' "Create test data on ${useDBName}.${tableName}......"
        executeSql "${sql}"
        showMsg 'errSysMsg' "Some error occur when execute '${sql}'"
        showMsg 'OK'
        # 创建索引（视情况决定是否打开）
        #showMsg 'msg2' "Create index on ${tableName}......"
        #sql="
        #     #create index idx_dept on ${tableName}(dept);
        #     #create index idx_create_time on ${tableName}(create_time);
        #     #create index idx_last_login_time on ${tableName}(last_login_time);
        #    "
        #executeSql "${sql}"
        #showMsg 'errSysMsg' "Some error occur when execute '${sql}'"
        #showMsg 'OK'
        showMsg 'msg' ''
}
 
#使用说明
function usage()
{
        parameter="$1"
        myFileName=`basename $0`
        if [ "${parameter}" = '--help'  -o  "${parameter}" = '-h' -o "${runBatch}" = "" ]; then
                echo "Usage:  sh ${myFileName} \${mysqlHost} \${mysqlPort} \${mysqlUser} \${mysqlPwd} \${DBName} \${tableName} \${runBatch}"
                echo "Usage1: sh ${myFileName} localhost 3306 root '123456' 'test' 'testTable' 20              # 在test库中生成testTable表，记录数为104万+"
                echo "Usage2: sh ${myFileName} localhost 3306 root '123456' 'test' 'testTable_{1..10}' 20      # 在test库中生成testTable_1、testTable_2......testTable_10共10张表，每表表记录数为104万+"
                echo "Usage2: sh ${myFileName} localhost 3306 root '123456' 'test' 'testTable_{01..10}' 20     # 在test库中生成testTable_01、testTable_02......testTable_10共10张表，每表表记录数为104万+"
                echo "        注意：'testTable_{1..10}' 要用单引号引起来"
                echo ''
                echo 'runBatch是循环次数：'
                echo '------------------------------------'
                echo '        runBatch=15生成32768记录'
                echo '        runBatch=16生成65536记录'
                echo '        runBatch=17生成13万+记录'
                echo '        runBatch=18生成26万+记录'
                echo '        runBatch=19生成52万+记录'
                echo '        runBatch=20生成104万+记录'
                echo '        runBatch=21生成209万+记录'
                echo '        runBatch=22生成419万+记录'
                echo '        runBatch=23生成838万+记录'
                echo '        runBatch=24生成1677万+记录'
                echo '        runBatch=25生成3355万+记录'
                echo '        runBatch=26生成6710万+记录'
                echo '        runBatch=27生成1.3亿+记录'
                echo ''
                exit 1
        fi
}
 
function main()
{
        # 初始化变量
        mysqlHost="$1"   # mysql Host
        mysqlPort="$2"   # mysql端口
        mysqlUser="$3"   # mysql账号
        mysqlPwd="$4"    # mysql密码
        useDBName="$5"   # 测试表所在的库名
        tableName="$6"   # 测试表表名
        runBatch="$7"    # 循环次数 runBatch=20生成104万记录；23生成838万记录，24生成1677万记录，25生成3300万记录...
        logFile="$8"
        #取得执行参数
        cmdShell=`basename $0`
        for theParameter in "$@"
        do
            parameterString="${parameterString} '${theParameter}'"
        done
        #输出帮助
        usage "$1"
        shellInit
        check
        #tableName='t_test{1..100}'
        isMoreTable=`echo "${tableName}" | grep -E '\{[0-9]+\.\.[0-9]+}' | wc -l`
        if [ "${isMoreTable}" = 1 ]; then
                tableBaseName=`echo $tableName | awk -F"{" '{print $1}'`
                rangeBegin=`echo "${tableName}" | awk -F"{" '{print $NF}' | awk -F"." '{print $1}' `
                # 如果分表的序号以0开头，则按rangeBegin的位数进行0填充，例如testTable_{01..10}，则生成的分表为testTable_01、testTable_02...testTable_10
                isZeroHead=`echo "${tableName}" | awk -F"{" '{print $NF}' | awk -F"." '{print $1}' | grep '^0' | wc -l`
                rangeBit=`echo ${#rangeBegin}`
                rangeEnd=`echo "${tableName}" | awk -F"{" '{print $NF}' | awk -F"." '{print $3}' | sed 's/}//g'`
                for i in `seq ${rangeBegin} ${rangeEnd}`; do
                        if [ "${isZeroHead}" = "1" ]; then
                                i=$(printf "%0${rangeBit}d" $i)
                        fi
                        tableTargetName="${tableBaseName}${i}"
                        createOneTableTestData "${tableTargetName}" "${runBatch}"
                done
        else
                createOneTableTestData "${tableName}" "${runBatch}"
        fi
}
main "$@"
```