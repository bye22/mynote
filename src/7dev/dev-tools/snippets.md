# markdown 代码片段支持设置
我们需要针对markdown类型文件进行具体的设置，打开settings.json文件，添加如下配置：
```
"[markdown]": {
    "editor.formatOnSave": true,
    "editor.renderWhitespace": "all",
    "editor.quickSuggestions": {
        "other": true,
        "comments": true,
        "strings": true
    },
    "editor.acceptSuggestionOnEnter": "on"
}
```
然后才能正常使用，已经配置的 `"scope": "markdown",`