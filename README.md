
/docs 查看api文档


# 安装

## docker安装
```
docker-compose build
docker-compose up
```

## 本地运行
```bash
virtualenv -p python3 env
source env3/bin/activate
pip install -r requirements.txt
./run.sh
```
访问 http://127.0.0.1:1100/admin 登录django

# 抓取数据
 ## 在docker 环境

```docker-compose up``启动系统， 
```docker exec -it xx bash```进入容器环境，
进入scrapyweixin目录
抓取微信文章
```bash
scrapy crawl weixin -a name='桂林电子科技大学'      #搜索抓取包含指定关键字的公众号
scrapy crawl wxarticle -a q='学生 打架'            #搜索抓取指定关键字的公众号文章
```

* 使用微博商业数据接口搜索
> 使用微博登录接口获取access_token，并写入weiboapi_search.py中
```bash
python weiboapi_search 桂林 学生    #搜索指定关键词结合的微博
```
