> https://cli.vuejs.org/zh/guide/cli-service.html#%E4%BD%BF%E7%94%A8%E5%91%BD%E4%BB%A4
# CLI 服务
# 使用命令
在一个 Vue CLI 项目中，@vue/cli-service 安装了一个名为 vue-cli-service 的命令。你可以在 npm scripts 中以 vue-cli-service、或者从终端中以 ./node_modules/.bin/vue-cli-service 访问这个命令。

`package.json`
```json
{
  "scripts": {
    "serve": "vue-cli-service serve",
    "build": "vue-cli-service build"
  }
}
```

```
npm run serve
# OR
yarn serve
```


vue-cli-service serve

```
用法：vue-cli-service serve [options] [entry]

选项：

  --open    在服务器启动时打开浏览器
  --copy    在服务器启动时将 URL 复制到剪切版
  --mode    指定环境模式 (默认值：development)
  --host    指定 host (默认值：0.0.0.0)
  --port    指定 port (默认值：8080)
  --https   使用 https (默认值：false)
  ```

  vue-cli-service build
  ```
  用法：vue-cli-service build [options] [entry|pattern]

选项：

  --mode        指定环境模式 (默认值：production)
  --dest        指定输出目录 (默认值：dist)
  --modern      面向现代浏览器带自动回退地构建应用
  --target      app | lib | wc | wc-async (默认值：app)
  --name        库或 Web Components 模式下的名字 (默认值：package.json 中的 "name" 字段或入口文件名)
  --no-clean    在构建项目之前不清除目标目录
  --report      生成 report.html 以帮助分析包内容
  --report-json 生成 report.json 以帮助分析包内容
  --watch       监听文件变化
  ```
```
  这里还有一些有用的命令参数：

--modern 使用现代模式构建应用，为现代浏览器交付原生支持的 ES2015 代码，并生成一个兼容老浏览器的包用来自动回退。

--target 允许你将项目中的任何组件以一个库或 Web Components 组件的方式进行构建。更多细节请查阅构建目标。

--report 和 --report-json 会根据构建统计生成报告，它会帮助你分析包中包含的模块们的大小。
```

vue-cli-service inspect

```
用法：vue-cli-service inspect [options] [...paths]

选项：

  --mode    指定环境模式 (默认值：development)
```

查看所有的可用命令

`npx vue-cli-service help`

`npx vue-cli-service help [command]`

缓存和并行处理

```
cache-loader 会默认为 Vue/Babel/TypeScript 编译开启。文件会缓存在 node_modules/.cache 中——如果你遇到了编译方面的问题，记得先删掉缓存目录之后再试试看。

thread-loader 会在多核 CPU 的机器上为 Babel/TypeScript 转译开启。
```

Git Hook

```
{
  "gitHooks": {
    "pre-commit": "lint-staged"
  },
   "lint-staged": {
    "*.{js,vue}": [
      "vue-cli-service lint",
      "git add"
    ]
  }
}
```