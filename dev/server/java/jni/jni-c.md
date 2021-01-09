# JNI with C

**Step 1: Write a Java Class HelloJNI.java that uses C Codes**
```java
public class HelloJNI {  // Save as HelloJNI.java
   static {
      System.loadLibrary("hello"); // Load native library hello.dll (Windows) or libhello.so (Unixes)
                                   //  at runtime
                                   // This library contains a native method called sayHello()
   }
 
   // Declare an instance native method sayHello() which receives no parameter and returns void
   private native void sayHello();
 
   // Test Driver
   public static void main(String[] args) {
      new HelloJNI().sayHello();  // Create an instance and invoke the native method
   }
}

```

**Step 2: Compile the Java Program HelloJNI.java & Generate the C/C++ Header File HelloJNI.h**

```bash
javac -h . HelloJNI.java
```

**Step 3: Implementing the C Program HelloJNI.c**

```c
// Save as "HelloJNI.c"
#include <jni.h>        // JNI header provided by JDK
#include <stdio.h>      // C Standard IO Header
#include "HelloJNI.h"   // Generated
 
// Implementation of the native method sayHello()
JNIEXPORT void JNICALL Java_HelloJNI_sayHello(JNIEnv *env, jobject thisObj) {
   printf("Hello World!\n");
   return;
}
```

**Step 4: Compile the C program HelloJNI.c**

(Windows) 64-bit JDK

```bat
x86_64-w64-mingw32-gcc -I"%JAVA_HOME%\include" -I"%JAVA_HOME%\include\win32" -shared -o hello.dll HelloJNI.c
```

(Windows) 32-bit JDK [Obsolete?]

```bat
i886-w64-mingw32-gcc -Wl,--add-stdcall-alias -I"%JAVA_HOME%\include" -I"%JAVA_HOME%\include\win32" -shared -o hello.dll HelloJNI.c
```

(Ubuntu) 64-bit JDK

/etc/profile or /home/[user]/.profile
```bash
#JDK环境变量
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk
export JRE_HOME=$JAVA_HOME/jre
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
export PATH=$PATH:$JAVA_HOME/bin
```
```bash
gcc -fPIC -I"$JAVA_HOME/include" -I"$JAVA_HOME/include/linux" -shared -o libhello.so HelloJNI.c
```

**Step 5: Run the Java Program**
```bash
java -Djava.library.path=. HelloJNI
```




