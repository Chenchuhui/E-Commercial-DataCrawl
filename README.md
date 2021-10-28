# E-Commercial-DataCrawl

简介：
本项目用于服务南非电商运营部门选品，并利用Django框架搭建后台管理系统。使用人员可以通过后台管理系统通过筛选选出理想的商品。这个功能将有效提高选品的效率，并赋能于公司其他部门。


配置环境：
需要python3以上版本。

所需要的包：requests，selenium，pymysql，threading，lxml

Django版本: 2.2


当前已有爬虫代码的南非独立站：KIKUU, FIX, JJHOUSE, SNATCHER, LOVELYWHOLE, KILIMALL, DEAL-HUB, VALUECO, JUMIA, BIDORBUY, ACKERMANS, CJDROPSHIPPING, MRP, ZANDO, YELLOWSUBTRADING （不排除这些网站会更新而导致代码没法用的情况）。

如果该网站是基于shopify建站，则可通过 https://github.com/lagenar/shopify-scraper.git 内的代码完成爬取。不需要重新编写爬虫代码。所有的爬虫代码在crawl/stage1 里面呈现。


