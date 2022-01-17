# golang环境变量配置
- 无图形桌面 
  -- 配置.profile文件 (需要重新登陆)
- 图形桌面配置
  -- 配置.xprofile文件 (需要重新登陆)
export GOROOT=/usr/local/go
export GOPATH=$HOME/GO_WORK
export PATH=$PATH:$GOROOT/bin
export GO111MODULE=on
export GOPROXY=https://goproxy.cn
- 查看已有配置命令
  ```
  go env
  ```

# go mod

go mod init awesome

- 常用命令
go mod download	下载依赖包到本地（默认为 GOPATH/pkg/mod 目录）
go mod edit	编辑 go.mod 文件
go mod graph	打印模块依赖图
go mod init	初始化当前文件夹，创建 go.mod 文件
go mod tidy	增加缺少的包，删除无用的包
go mod vendor	将依赖复制到 vendor 目录下
go mod verify	校验依赖
go mod why	解释为什么需要依赖

# golang交叉编译命令
Mac 下编译 Linux 和 Windows 64位可执行程序
```
CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build main.go
CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go build main.go
```
Linux 下编译 Mac 和 Windows 64位可执行程序
```
CGO_ENABLED=0 GOOS=darwin GOARCH=amd64 go build main.go
CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go build main.go
```
Windows 下编译 Mac 和 Linux 64位可执行程序
```
SET CGO_ENABLED=0
SET GOOS=darwin
SET GOARCH=amd64
go build main.go

SET CGO_ENABLED=0
SET GOOS=linux
SET GOARCH=amd64
go build main.go
```
---
GOOS：目标平台的操作系统（darwin、freebsd、linux、windows）
GOARCH：目标平台的体系架构（386、amd64、arm）
交叉编译不支持 CGO 所以要禁用它

# 资料网址

[go编程规约]https://www.jianshu.com/p/165001950939

[goenv]https://wiki.jikexueyuan.com/project/go-command-tutorial/0.14.html

[GolangGtk+3教程：开始]https://www.cnblogs.com/xiyu714/p/9895614.html
