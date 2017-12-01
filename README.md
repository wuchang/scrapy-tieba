
/docs 查看api文档


# 安装

## docker运行
```
docker-compose build
docker-compose up
docker-compose exec app python yqadmin/manage.py migrate            #更新数据库
docker-compose exec app python yqadmin/manage.py createsuperuser    #创建django管理员用户
docker-compose exec app /bin/bash -c 'cd scrapytieba &&  scrapy crawl tieba'    #在容器中执行tieba爬虫

```


## 本地运行
```bash
virtualenv -p python3 env
source env3/bin/activate
pip install -r requirements.txt
./run.sh
```
访问 http://127.0.0.1:1100/admin 登录django
 