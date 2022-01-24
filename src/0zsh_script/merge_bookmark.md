# 合并书签并文件名分隔

```zsh
awk 'tmp!=FILENAME{tmp=FILENAME;print "\n<hr><br>"tmp":\n<hr><br>"} {print "\t"$0}' * >>../index.md
```

# 词云生成

```zsh
wordcloud_cli --text ~/Desktop/index.txt --repeat --width 800 --height 400 --max_words 100 --min_word_length 3 --no_collocations  --stopwords  ~/Desktop/stop_words.txt  --imagefile ~/Desktop/cloud.jpg
```



