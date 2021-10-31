from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

url = "https://dex.guru/token/0xa25610a77077390a75ad9072a084c5fbc7d43a0d-polygon"
url = "https://dex.guru/token/0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0-eth"
lots = [500]
"""
#proxy settings ちょっと古いかもしれんが、とりあえず動く。→動かなくなった！
proxy = "185.61.152.137:8080"
firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True

firefox_capabilities['proxy'] = {
    "proxyType": "MANUAL",
    "httpProxy": proxy,
    "sslProxy": proxy
}
driver = webdriver.Firefox(capabilities=firefox_capabilities)
"""
def sleep(sleeptime):
    print("Sleep for "+ str(sleeptime)+" second(s)!!")
    time.sleep(sleeptime)
    print("awake!!")

driver = webdriver.Firefox()
#driver.set_window_size(1400,600)
driver.set_window_size(1100,800)
driver.get(url)
sleep(5)

togglebutton = driver.find_element(By.CLASS_NAME,"tradeform-combo__toggle")
togglebutton.click()
sleep(0.5)

#usdtbutton = driver.find_element(By.XPATH,"//button[@data-id='0xc2132d05d31c914a87c6611c10748aeb04b58e8f-polygon']")
usdtbutton = driver.find_element(By.XPATH,"//button[@data-id='0xdac17f958d2ee523a2206206994597c13d831ec7-eth']")
usdtbutton.click()
sleep(0.5)

#buy price
buytab = driver.find_element(By.CLASS_NAME,"tradeform-tab--buy")
priceinput = buytab.find_element(By.CLASS_NAME,"tradeform-field__input")
priceinput.send_keys(lots[0])
sleep(5)

pricefield = driver.find_elements(By.XPATH,"//input[@readonly='']")[0]
buyprice = lots[0]/float(pricefield.get_attribute('title'))
print('buy price: ' + str(buyprice))


sellbutton = driver.find_element(By.XPATH,"//label[@for='tradeform-tab__toggle--sell']")
sellbutton.click()
sleep(0.5)

#sell price
selltab = driver.find_element(By.CLASS_NAME,"tradeform-tab--sell")
priceinput = selltab.find_element(By.CLASS_NAME,"tradeform-field__input")
priceinput.send_keys(round(lots[0]/buyprice,4))
sleep(5)

pricefield = driver.find_elements(By.XPATH,"//input[@readonly='']")[1]
print(pricefield)
print(round(lots[0]/buyprice,4))
sellprice = float(pricefield.get_attribute('title'))/(round(lots[0]/buyprice,4))
print('sell price: ' + str(sellprice))

sleep(60)
driver.quit()

"""
search = driver.find_element_by_name('q')
search.send_keys(keyword)
search.submit()

time.sleep(3)
soup = BeautifulSoup(driver.page_source, 'html.parser')
results = soup.find_all("a", attrs={"class":"result__a"})

print(results)

for i, result in enumerate(results):
    print("%d: %s" % (i+1, result.get_text()))

time.sleep(5)
driver.quit()
"""
