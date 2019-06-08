# 50 Years 50 Prolific Authors in Remote Sensing of Environment
In terms of impact factor, Remote Sensing of Environment has been consistently ranked as NO.1 remote sensing journal over the past decade. I wrote a spider to crawl its website and extract all available author information. Web scrapying code can be found in this [folder](https://github.com/RickWeng/web-scraping-rse/tree/master/rse). Please click [here](https://nbviewer.jupyter.org/github/RickWeng/web-scraping-rse/blob/master/50years50authors-rse.ipynb) to view the data processing code. 
## Web Scrapying
https://www.sciencedirect.com/journal/remote-sensing-of-environment/issues contains information of issues from 1969 to 2019. 
By the date (Jun 6th 2019) of web scraping, the most recent volume was Volume 231 (in progress 15 September 2019).
`Scrapy` web scrapying framework and `Selenium` package in Python were used to extract data from the journal web. `Selenium` was used to automatically click each button to show the hidden urls.   
Some prerequisites were listed below:   
* run in terminal: 
```
pip3 install scrapy selenium 
```
* Download web driver (Firefox driver for me)   
* run in terminal: 
```
sudo cp geckodriver's position /usr/local/bin
sudo chmod +x /usr/local/bin/geckodriver
```
* In settings.py, change `ROBOTSTXT_OBEY = True` to `ROBOTSTXT_OBEY = False`
## Results
