import scrapy

class allspider(scrapy.Spider):
    name = 'allspider'
    start_urls = [
        'http://lab.scrapyd.cn'
    ]

    def parse(self, response):
        '''查询是否还有下一页，如果有接着爬取下一页'''
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        mingyan = response.css('div.quote')
        for v in mingyan:
           text = v.css('.text::text').extract_first()
           author = v.css('.author::text').extract_first()
           tags = v.css('.tags .tag::text').extract()
           tags = ','.join(tags)

           filename = '%s-语录.txt' % author
           with open(filename, 'a+') as f:
               f.write(text)
               f.write('\n')
               f.write('标签：'+ tags)
               f.write('\n----------\n')
               f.close()