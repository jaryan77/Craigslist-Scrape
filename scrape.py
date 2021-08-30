import time
import datetime
import pandas as pd
import requests
from bs4 import BeautifulSoup

# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
#     'Connection': 'keep-alive'
# }


#Get first page of vehicle listings in chicago (filtered by 'owner' and only listings with image)
base_url = 'https://chicago.craigslist.org/d/cars-trucks-by-owner/search/cto?hasPic=1'

respone = requests.get(base_url)
soup = BeautifulSoup(respone.content, 'html.parser')



