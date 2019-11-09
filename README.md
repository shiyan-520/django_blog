#### 项目介绍：

本源码是基于 Django2.2 + Python3 + [Hacker](https://github.com/CodeDaraW/Hacker/) 编写的博客源码，整体前端样式和当前个人 Hexo + Github 搭建的博客一致。

目前该源码为第一版，后续会对源码进行优化，主要优化点在于 “搜索”、“数据库”、“安全”、“数据分析展示”、“缓存机制” 等等方面。

#### 使用介绍：

注：线上实际部署，请直接百度相关部署教程。

搭建使用前，需要安装一下三方模块：django_ckeditor==5.7.1、Django==2.2.7

**本地源码展示使用以下命令：**

python3 manage.py runserver 8080 --insecure

**修改博客首页显示文章数据：**

路径：sh1yanblog\index\views.py   第十一行

paging_list = Paginator(cus_list,6,1) # 这里用来设置首页显示多少文章

**后台账号密码：**
账号：admin
密码：administrator




