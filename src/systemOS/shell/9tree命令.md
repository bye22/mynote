```shell
tree -fI  ".vscode|work|_book|node_modules|book.json|package*|SUMMARY.md" -P "*.md"  > README.md
```
> `-f` 相对路径
> `-I` 排除路径或文件
> `-P` 包含文件或路径