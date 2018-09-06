import  scrapy

class itemspider(scrapy.Spider):
    name = 'itemspider'
    start_urls = ['http://lab.scrapyd.cn']

    def parse(self, response):
        mingyan = response.css('div.quote')[3]
        text = mingyan.css('.text::text').extract_first()
        author = mingyan.css('.author::text').extract_first()
        tags = mingyan.css('.tags .tag::text').extract()
        tags = ','.join(tags)

        filename = '%s-语录.txt' % author
        f = open(filename, "a+")
        f.write(text)
        f.write('\n')
        f.write('标签：'+ tags )
        f.close()
