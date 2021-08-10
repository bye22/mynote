# 常用插件
Chinese 简体中文


# vue
`npm install --registry=https://registry.npm.taobao.org`



npm config ls 查看


`npm install -g @vue/cli`


# npm降级
Module not found: Error: Can't resolve 'core-js/es6'

npm i -S core-js@2.5.7 
或 npm i -S core-js@2


# npm设置源地址

-- 查看当前地址：
npm config get registry
https://registry.npmjs.org/
 
npm config get disturl
undefined
 
 
-- 设置当前地址（设置为淘宝镜像）
npm config set registry http://registry.npm.taobao.org/
 
-- 设置当前地址（设置为默认地址）
npm config set registry https://registry.npmjs.org/
 
-- 每次执行命令前加入–registry指定仓库路径
npm --registry https://registry.npm.taobao.org install
 
# 使用nrm工具切换淘宝源
npx nrm use taobao
 
# 如果之后需要切换回官方源可使用
npx nrm use npm
