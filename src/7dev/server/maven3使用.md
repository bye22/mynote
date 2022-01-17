# 打入本地jar
mvn install:install-file -Dfile=/home/cogs/Downloads/cpcn-payment-api-2.2.1.jar -DgroupId=payment.api -DartifactId=cpcn-payment-api -Dversion=2.2.1 -Dpackaging=jar


mvn install:install-file -Dfile=/home/cogs/Downloads/pushlet-2.0.4.jar -DgroupId=nl.justobjects.pushlet -DartifactId=pushlet -Dversion=2.0.4 -Dpackaging=jar

mvn install:install-file -Dfile=/home/cogs/Downloads/tools-1.6.9.jar -DgroupId=payment.tools -DartifactId=tools -Dversion=1.6.9 -Dpackaging=jar

mvn install:install-file -Dmaven.repo.local=/home/cogs/.m2/jeecg -Dfile=/home/cogs/Downloads/qiniu-java-sdk-7.2.23.jar -DgroupId=com.qiniu -DartifactId=qiniu-java-sdk -Dversion=7.2.23 -Dpackaging=jar

## 多线程编译并跳过测试
alias mvn1C="mvn -T 1C clean install -Dmaven.compile.fork=true -Dmaven.test.skip=true"

## 多线程编译，跳过测试，排除多个子模块
alias mvnSkipMod1C="mvn -T 1C -pl '!web-html,!web-wechat' clean install -Dmaven.compile.fork=true -Dmaven.test.skip=true"
