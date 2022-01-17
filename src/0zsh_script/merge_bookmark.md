# 合并书签并文件名分隔

```zsh
awk 'tmp!=FILENAME{tmp=FILENAME;print "\n<hr><br>"tmp":\n<hr><br>"} {print "\t"$0}' * >../index.md
```