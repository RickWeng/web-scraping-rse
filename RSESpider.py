import scrapy
import re
from selenium import webdriver
from scrapy import Selector
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class RSESpider(scrapy.Spider):
    name = "RSE"
    urls = []
    for i in range(1, 4):
        urls.append('https://www.sciencedirect.com/journal/remote-sensing-of-environment/issues?page={}'.format(i))
    start_urls = urls
    
    def parse(self, response):
        driver = webdriver.Firefox()
        driver.get(response.url)
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='0-accordion-tab-1']")))
        if response.url != 'https://www.sciencedirect.com/journal/remote-sensing-of-environment/issues?page=3':
            for i in range(19, 0, -1):
                click_button = "(.//*[normalize-space(text()) and normalize-space(.)='Previous'])[1]/preceding::span[{}]".format(i)
                driver.find_element_by_xpath(click_button).click()
            # Wait as long as required, or maximum of 5 sec for element to appear
            # If successful, retrieves the element
        else:
            for i in range(8, 0, -1):
                click_button = "(.//*[normalize-space(text()) and normalize-space(.)='Previous'])[1]/preceding::span[{}]".format(i)
                driver.find_element_by_xpath(click_button).click()

        html = driver.page_source 
        sel = Selector(text=html)
        driver.quit()

        links = sel.xpath('//a[@class="anchor text-m"]/@href').extract() 

        for link in links:
            yield response.follow(link, self.parse_info)
    
    def parse_info(self, response):
        rse_authors = response.xpath('//div[@class="text-s u-clr-grey8 js-article__item__authors"]/text()').extract()
        rse_year = response.xpath('//h3[@class="js-issue-status text-s"]/text()').extract()
        
        for author in rse_authors:   
            yield {
            'author': author,
            'year': rse_year
            }

# run in terminal: scrapy runspider rse/spiders/RSESpider.py  -o res.csv




