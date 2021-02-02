mvn install:install-file -Dfile=/home/cogs/Downloads/cpcn-payment-api-2.2.1.jar -DgroupId=payment.api -DartifactId=cpcn-payment-api -Dversion=2.2.1 -Dpackaging=jar


mvn install:install-file -Dfile=/home/cogs/Downloads/pushlet-2.0.4.jar -DgroupId=nl.justobjects.pushlet -DartifactId=pushlet -Dversion=2.0.4 -Dpackaging=jar

mvn install:install-file -Dfile=/home/cogs/Downloads/tools-1.6.9.jar -DgroupId=payment.tools -DartifactId=tools -Dversion=1.6.9 -Dpackaging=jar

mvn install:install-file -Dmaven.repo.local=/home/cogs/.m2/jeecg -Dfile=/home/cogs/Downloads/qiniu-java-sdk-7.2.23.jar -DgroupId=com.qiniu -DartifactId=qiniu-java-sdk -Dversion=7.2.23 -Dpackaging=jar