import scrapy

class firstscrapy(scrapy.Spider):

    name = 'firstscrapy' #定义蜘蛛名

    # def start_requests(self):
    #     urls = [
    #         'http://lab.scrapyd.cn/page/1/',
    #         'http://lab.scrapyd.cn/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)
    start_urls=[
        'http://lab.scrapyd.cn/page/1/',
        'http://lab.scrapyd.cn/page/2/',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename='firstscrapy-%s.html' % page
        with open(filename ,'wb') as f:
            f.write(response.body)

        self.log('保存文件：%s'%filename)
