from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.get('https://www.nzpyq.com')
# driver.refresh()
time.sleep(3)
# Agencies = driver.find_element_by_xpath("/html/body/#root/div[0]/jss117/ul.MuiList-root jss127 MuiList-padding/li.MuiListItem-root jss129 MuiListItem-gutters/a.jss131/").click()
# click girls
driver.find_element_by_link_text("GIRLS").click()
#click pictures
# driver.find_element_by_xpath("//*[@id='root']/div[3]/div[4]/div[5]/div/button").click()
#search Auckland girls
search=driver.find_element_by_xpath("//*[@id='root']/div[3]/div[1]/div/div/div[2]/div/div[1]/div/div").click()
driver.find_element_by_xpath("//*[@id='menu-']/div[3]/ul/li[2]").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='root']/div[3]/div[1]/div/div/div[2]/div/div[5]/button/span[1]").click()

time.sleep(3)
#click love girls

# Love_Girls=driver.find_element_by_xpath('//*[@id="root"]/div[3]/div[2]/div/div/div[2]/div/div[6]/div/div/a')
# Love_Girls.click()
# click vip girls
driver.find_element_by_xpath('//*[@id="root"]/div[3]/div[4]/div[1]/div/button').click()
#click to another page
time.sleep(5)
driver.find_element_by_link_text('LIKES').click()