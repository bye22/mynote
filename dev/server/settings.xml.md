```xml
<?xml version="1.0" encoding="UTF-8" ?>
<settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0 http://maven.apache.org/xsd/settings-1.0.0.xsd">

    <!--自定义本地仓库路径-->
    <localRepository>/home/cogs/.m2/repository</localRepository>

    <mirrors>

       <!--默认的中央仓库-->
   	    <mirror>
   	        <id>mirrorId</id>
   	        <mirrorOf>central,alimaven</mirrorOf>
   	        <name>Human Readable Name for this Mirror.</name>
   	        <url>https://repo.maven.apache.org/maven2/</url>
  	    </mirror>
 	    <mirror>
	        <id>alimaven</id>
	    	<name>aliyun maven</name>
	    	<url>https://maven.aliyun.com/repository/public</url>
 	    	<mirrorOf>central</mirrorOf>
	    </mirror>


        <mirror>
            <id>repo.exist.com</id>
            <mirrorOf>central</mirrorOf>
            <url>http://repo.exist.com/maven2</url>
        </mirror>
        <mirror>
            <id>ibiblio.org</id>
            <mirrorOf>central</mirrorOf>
            <url>http://mirrors.ibiblio.org/pub/mirrors/maven2</url>
        </mirror>
        <mirror>
            <id>ibiblio.net</id>
            <mirrorOf>central</mirrorOf>
            <url>http://www.ibiblio.net/pub/packages/maven2</url>
        </mirror>
        <mirror>
            <id>uk.maven.org</id>
            <mirrorOf>central</mirrorOf>
            <url>http://uk.maven.org/maven2</url>
        </mirror>

    </mirrors>


  
</settings>
```