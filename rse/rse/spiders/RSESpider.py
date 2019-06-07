# run in terminal: pip3 install scrapy selenium 
# download Firefox driver
# run in terminal: sudo cp geckodriver's position /usr/local/bin
                 # sudo chmod +x /usr/local/bin/geckodriver
# enable Katalon Recorder extension in Firefox

import scrapy 
from scrapy import Selector
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re

# run in terminal: scrapy startproject rse
# change in settings.py: ROBOTSTXT_OBEY = False

# RSE spider
class RSESpider(scrapy.Spider):
    name = "RSE"
    urls = []
    for i in range(1, 4):
        urls.append(
            'https://www.sciencedirect.com/journal/remote-sensing-of-environment/issues?page={}'.format(i)
            )
    start_urls = urls
    
    # crawl journal issue links
    def parse(self, response):
        # automatically click all navigation down buttions to show hidden links
        driver = webdriver.Firefox()
        driver.get(response.url)
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@id="0-accordion-tab-1"]'))
            )
        # wait as long as required, or maximum of 3 sec for element to be clickable
        # if successful, click the button
        # use Katalon Recorder to export test case as script
        if response.url != 'https://www.sciencedirect.com/journal/remote-sensing-of-environment/issues?page=3':
            for i in range(19, 0, -1):
                click_button = "(.//*[normalize-space(text()) and normalize-space(.)='Previous'])[1]/preceding::span[{}]".format(i)
                driver.find_element_by_xpath(click_button).click()
            
        else:
            for i in range(8, 0, -1):
                click_button = "(.//*[normalize-space(text()) and normalize-space(.)='Previous'])[1]/preceding::span[{}]".format(i)
                driver.find_element_by_xpath(click_button).click()
        # crawl links
        html = driver.page_source 
        sel = Selector(text=html)
        driver.quit()

        links = sel.xpath('//a[@class="anchor js-issue-item-link text-m"]/@href').extract() 

        for link in links:
            yield response.follow(link, self.parse_info)
    
    # crawl author, year and volume information
    def parse_info(self, response):
        rse_authors = response.xpath('//div[@class="text-s u-clr-grey8 js-article__item__authors"]/text()').extract()
        rse_years = response.xpath('//h3[@class="js-issue-status text-s"]/text()').extract()
        year = rse_years[0][-5:-1]
        rse_volumes = response.xpath('//h2[@class="u-text-light u-h1 js-vol-issue"]/text()').extract()
        volume = re.split(r'\s', rse_volumes[0])[1].split(',')[0]
        for author in rse_authors:   
            yield {
            'author': author,
            'year': year,
            'volume': volume
            }

# run in terminal: scrapy runspider rse/spiders/RSESpider.py  -o result.csv




