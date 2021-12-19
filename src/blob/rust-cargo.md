# rust代理配置
```
[source.crates-io]
registry = "https://github.com/rust-lang/crates.io-index"
# 指定镜像
replace-with = 'sjtu'

# 清华大学
[source.tuna]
registry = "https://mirrors.tuna.tsinghua.edu.cn/git/crates.io-index.git"

# 中国科学技术大学
[source.ustc]
registry = "git://mirrors.ustc.edu.cn/crates.io-index"

# 上海交通大学
[source.sjtu]
registry = "https://mirrors.sjtug.sjtu.edu.cn/git/crates.io-index"

# rustcc社区
[source.rustcc]
registry = "https://code.aliyun.com/rustcc/crates.io-index.git"
```
# cargo常用命令
```
cargo new hello_world --bin
cargo new hello_world --lib
cargo new hello_world --lib --vcs none
cargo build --release
cargo run


cargo update           # updates all dependencies
cargo update -p rand   # updates just “rand”

cargo install --git https://hub.fastgit.org/hecrj/iced.git iced
```

# rustup常用命令

> stable beta nightly
```
rustup default stable
rustup override set nightly
```