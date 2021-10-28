# E-Commercial-DataCrawl

简介：
本项目用于服务南非电商运营部门选品，并利用Django框架搭建后台管理系统。数据库将存储所有爬取到的数据并通过后台管理系统可视化。使用人员可以通过后台管理系统通过筛选选出理想的商品。这个功能将有效提高选品的效率，并赋能于公司其他部门。


配置环境：
需要python3以上版本。

所需要的包：requests，selenium，pymysql，threading，lxml

Django版本: 2.2


当前已有爬虫代码的南非独立站：KIKUU, FIX, JJHOUSE, SNATCHER, LOVELYWHOLE, KILIMALL, DEAL-HUB, VALUECO, JUMIA, BIDORBUY, ACKERMANS, CJDROPSHIPPING, MRP, ZANDO, YELLOWSUBTRADING （不排除这些网站会更新而导致代码没法用的情况）。

如果该网站是基于shopify建站，则可通过 https://github.com/lagenar/shopify-scraper.git 内的代码完成爬取。不需要重新编写爬虫代码。所有的爬虫代码在crawl/stage1 里面呈现。


爬虫代码分为三个阶段。第一阶段是爬取南非独立站，我们获得每个商品独立的ID，标题，价格，和最重要的图片链接。ID作为唯一的标识符，可以用作去重的标准。

第二阶段通过调取1688api: https://open.1688.com/api/apiTool.htm?ns=com.alibaba.linkplus&n=alibaba.cross.similar.offer.search&v=1 ，从而通过图片获取相关供应商的信息。可以按照公司的需求选取销量优先还是价格低廉优先。

第三阶段
