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