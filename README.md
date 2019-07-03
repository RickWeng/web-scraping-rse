# 50 Years 50 Prolific Authors in Remote Sensing of Environment
In terms of impact factor, Remote Sensing of Environment has been consistently ranked as NO.1 remote sensing journal over the past decade. I wrote a spider to crawl its website and extract all available author information. Web scrapying code can be found in this [folder](https://github.com/RickWeng/web-scraping-rse/tree/master/rse). Please click [here](https://github.com/RickWeng/web-scraping-rse/blob/master/50years50authors-rse.ipynb) to view the data processing code. 
## Web Scrapying
https://www.sciencedirect.com/journal/remote-sensing-of-environment/issues contains information of issues from 1969 to 2019. 
`Scrapy` web scrapying framework and `Selenium` package in Python were used to extract data from the journal web. `Selenium` was used to automatically click each button to show the hidden urls.   
![](https://github.com/RickWeng/web-scraping-rse/blob/master/scrapylogo.png)    
![](https://github.com/RickWeng/web-scraping-rse/blob/master/seleniumlogo.png)    
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

All codes are available in this [folder](https://github.com/RickWeng/web-scraping-rse/tree/master/rse).   
## Results
By the date (Jun 6th 2019) of web scraping, the most recent volume was Volume 231 (in progress 15 September 2019). Information of around 7000 papers was extracted. It should be noted that only the first three authors were considered in the analysis since for each article only five authors at most are available on their website. "min" rank method (i.e. rank the dataframe by minimum rank if 2 or more values are found to be the same) was used so top 50 authors may have more than 50 authors. For example:   ]

| Author | Num_Publications | Rank |
|:------:|:----------------:|:----:|
| A      | 20               | 1    |
| B      | 20               | 1    |
| C      | 18               | 3    |

### Top 50 Prolific Authors in Remote Sensing Environment (1969 - 2019)
![](https://github.com/RickWeng/web-scraping-rse/blob/master/figures/top-50-author.png)
### Top 50 Prolific Authors in Remote Sensing of Environment Over the Past Decade (2010 - 2019)
The figure was sorted in descending order by the total number of publications over the past decade.
![](https://github.com/RickWeng/web-scraping-rse/blob/master/figures/top-50-author-1019.png)
### Top 50 Prolific First Authors in Remote Sensing Environment (1969 - 2019)
![](https://github.com/RickWeng/web-scraping-rse/blob/master/figures/top-50-first-author.png)
