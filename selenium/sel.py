from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

#PLEASE SPECIFY CHROME PATH EXECUTABLE
chrome_path = '/Users/mateusz/Documents/Learning/WSSMS/class_07/chromedriver'
url = 'https://conotoxia.com/cryptocurrencies/cryptocurrency-rates'

LIMIT_PAGES = 4
url = 'https://conotoxia.com/cryptocurrencies/cryptocurrency-rates'
urls = [url+'/p/'+str(i) for i in range(1, LIMIT_PAGES+1)]
names = ["currency", "average_rate", "market_value", "volume", "exchange"]
df = pd.DataFrame(dict(zip(names, [[]]*4 )))

for url in urls:
    chrome_options = Options()  
    chrome_options.add_argument("--headless")  
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_path)
    driver.get(url)

    for tr in driver.find_elements_by_tag_name("tr")[1:]:
        values = []
        for td in tr.find_elements_by_tag_name("td"):
            attr = td.get_attribute("innerText")
            val = ''.join([x for x in attr if ord(x) < 127]).replace("\n","")
            values.append(val)

        row = dict(zip(names, values))
        df = df.append(row, ignore_index=True)
df.to_csv("crypto.csv", index=False)
driver.quit()
