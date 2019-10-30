###创建商户
from selenium import webdriver
import time
import selenium.webdriver.support.ui as ui
driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.get('https://user.nzpyq.com')
#log in
driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/form/div[1]/div[2]/div/span/input').send_keys('225851213')
driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/form/div[2]/div[2]/div/span/input').send_keys('111111')
driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/form/div[4]/div/div/span/button').click()
time.sleep(3)
#click create user
driver.find_element_by_xpath('//*[@id="root"]/section/aside/div[1]/div[2]/div/div/ul/li[2]/a').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/form/div[1]/div[2]/div/span/span/input').send_keys('a@qq.com')
driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/form/div[6]/div[2]/div/span/div/div/div').click()
# wait = ui.WebDriverWait(driver,10)
# wait.until(lambda driver: driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/form/div[1]/div[2]/div/span/span/input'))
driver.refresh()
time.sleep(2)
# driver.find_element_by_xpath('/html[1]/body[1]/div[1]/section[1]/section[1]/main[1]/div[1]/form[1]/div[1]/div[2]/div[1]/span[1]/span[1]/input[1]').send_keys('aa@qq.com')
driver.find_element_by_xpath("//input[@placeholder='请输入商户邮箱']").send_keys('aa@wew.com')
driver.find_element_by_xpath("//input[@placeholder='请输入商户手机号码']").send_keys('123456')
driver.find_element_by_xpath("//input[@placeholder='请输入First Name']").send_keys('qa')
driver.find_element_by_xpath("//input[@placeholder='请输入Last Name']").send_keys('qwee')
driver.find_element_by_xpath("//input[@placeholder='请输入商户密码']").send_keys('12345a')
driver.find_element_by_xpath("//div[@class='ant-select-selection__rendered']").click()
driver.find_element_by_xpath("//li[contains(text(),'Wellington')]").click()
time.sleep(2)
driver.find_element_by_xpath("//button[@class='ant-btn']").click()

time.sleep(2)
#input user information
# driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/form/div[7]/div/div/span/button').cli

# driver.find_element_by_xpath('/html[1]/body[1]/div[1]/section[1]/section[1]/main[1]/div[1]/form[1]/div[4]/div[2]/div[1]/span[1]/input[1]').send_keys('aa@qq.com')