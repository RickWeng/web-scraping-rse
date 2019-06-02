import scrapy
import re
# Import the CrawlerProcess
from scrapy.crawler import CrawlerProcess
import pandas as pd
class RSESpider(scrapy.Spider):
    name = "RSE"
    start_urls = [
            'https://www.sciencedirect.com/journal/remote-sensing-of-environment/issues'
        ]
    def parse(self, response):
        urls = response.xpath('//a[@class="anchor text-m"]/@href').extract()    # find all sub urls
        for url in urls:
            yield response.follow(url, callback=self.parse_info)
    
    def parse_info(self, response):  
        rse_df=[]  
        if response.xpath('//dd[@class="js-article-author-list u-clr-grey8 text-s"]/text()') is not None:
            rse_titles = response.xpath('//span[@class="js-article-title"]/text()').extract()
            rse_authors = response.xpath('//div[@class="text-s u-clr-grey8 js-article__item__authors"]/text()').extract()
            rse_year = response.xpath('//h3[@class="js-issue-status text-s"]/text()').extract()
            for rse_title, rse_author in zip(rse_titles, rse_authors):
                rse_df2 = rse_df.append(pd.DataFrame(list(zip(rse_title,rse_author)), columns=['tilte', 'author']))
            yield rse_df2


# run in terminal: scrapy runspider rse/spiders/RSESpider.py  -o res.csv




