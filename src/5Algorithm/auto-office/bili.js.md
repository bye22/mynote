# node图片爬虫

```js
const request = require('superagent');
const fs = require('fs-extra');
const path = require('path');
const awaitWriteStream = require('await-stream-ready').write;
const ProgressBar=require('../module/process-bar');

// 初始化一个进度条ProgressBar 实例
let pb = new ProgressBar('下载进度', 0);

//初始化爬取url地址
const url = 'https://api.vc.bilibili.com/link_draw/v1/doc/doc_list?uid=6823116&page_num=0&page_size=500&biz=all';

//初始化header
const uag='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36';
const accept='text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9';

//初始化图片存储路径
const parentPath="/home/cogs";
const imagePath="images";


async function getUrlAndName(){
    // 用于存储返回值
    let imgAddrArray = [];
    // 请求资源
    const res = await request.get(url)
        .set({
            'User-Agent': uag,
            'Accept': accept,
        }).timeout({ response: 500, deadline: 60000 });
    let res_json = JSON.parse(res.text);
    let res_info = res_json.data.items;
    res_info.map((res_info_value, _res_info_index)=>{
        let pic_description = res_info_value.title+res_info_value.description;
        res_info_value.pictures.map((pic_url, pic_index)=>{
            let url_list = pic_url.img_src.split(".");
            let file_ext = url_list[url_list.length-1];
            imgAddrArray.push([pic_url.img_src, pic_description+"-"+pic_index+Date.parse(new Date())+"."+file_ext]);
        });
    });
    return imgAddrArray;
}
/**
 *  下载图片
 * @param {*} imgAndName 
 */
async function download(imgAndName){
    /* 拼接出, 当前资源的文件名 */
    let filename = imgAndName[1];
    /* 创建读取流 */
    const rs = request.get(imgAndName[0]);

    const ws = fs.createWriteStream(path.join(parentPath, imagePath, filename));
    console
    let bilibili_stream = rs.pipe(ws);
    ws.on('finish', ()=>{
        return filename;
    });
    await awaitWriteStream(bilibili_stream);
}
/**
 * 创建文件夹, 控制整体流程
 */
async function init(){
    /* 创建文件夹 */
    try{
        await fs.mkdirs(path.join(parentPath, imagePath));
        console.log("创建图片文件夹 : "+path.join(parentPath, imagePath))
    }
    catch(err){
        console.log("==>", err);
    }

    let imgAddrArray = await getUrlAndName();
 
    console.log("开始下载...")
    console.log("显示当前下载进度...");
    for (let i=0; i<imgAddrArray.length; i++){
        try{
            let result = await download(imgAddrArray[i]);
            let count=i+1;
            let totall=imgAddrArray.length;
            /* 加载终端进度条 */
            pb.render({ completed: count, total: totall });
        }
        catch(err){
            console.log("err==>", err);
        }
    }
}

/* 函数调用 */
init();
```