from bs4 import BeautifulSoup as BS
from numpy import column_stack
from urllib import request as re
import pandas as pd
from urllib.request import Request, urlopen

LIMIT_PAGES = 4
url = 'https://conotoxia.com/cryptocurrencies/cryptocurrency-rates'
urls = [url+'/p/'+str(i) for i in range(1, LIMIT_PAGES+1)]
print(urls)

names = ["currency", "average_rate", "market_value", "volume", "exchange"]
df = pd.DataFrame(dict(zip(names, [[]]*4 )))

for url in urls:
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BS(webpage, 'html.parser')

    for tr in soup.find_all('tr')[1:]:
        tds = tr.find_all('td')
        values = []
        for i in range(len(tds)):
            values.append(''.join([x for x in tds[i].text if ord(x) < 127]).replace("\n",""))
        row = dict(zip(names, values))
        print(row)
        df = df.append(row, ignore_index=True)
df.to_csv("project_scrapping//bs//crypto.csv", index=False)
