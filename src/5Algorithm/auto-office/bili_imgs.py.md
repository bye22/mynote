# python图片爬虫

```py
# -*- coding:UTF-8 -*-
import requests, json, time, sys
from contextlib import closing

url = 'https://api.vc.bilibili.com/link_draw/v1/doc/doc_list?uid=6823116&page_num=0&page_size=500&biz=all';

def getUrlAndName():
    # 用于存储返回值
    imgAddrArray = [];
    
    headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        }
    # 请求资源
    res = requests.get(url,headers=headers)
#     res_json = json.loads(res.text)
    res_json = res.json()
    #print(res_json['data']['items'])
    for x in res_json['data']['items']:
        #print(x['pictures'])
        print(x['description'])
        for y in x['pictures']:
            print(y['img_src'])
if __name__ == '__main__':
    getUrlAndName()
```
