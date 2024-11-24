import requests
from lxml import etree
import pandas as pd
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

def get_data(html,data_list):
    selector = etree.HTML(html)
    data = selector.xpath('//*[@id="content"]/div/div[1]/ol/li')
    for item in data:
        title = item.xpath('.//div[@class="hd"]/a/span[1]/text()')[0]
        score = item.xpath('.//span[@class="rating_num"]/text()')[0]
        quote = item.xpath('.//span[@class="inq"]/text()')
        print(title, score, quote)
        data_list.append([title, score, quote])

data_list = []

for i in range(0, 100, 25):
    url = 'https://movie.douban.com/top250?start=' + str(i)
    res = requests.get(url, headers=headers)
    html = res.content.decode('utf-8')
    get_data(html, data_list)

df = pd.DataFrame(data_list, columns=['title', 'score', 'quote'])
df.to_excel('douban.xlsx', index=False)