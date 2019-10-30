from selenium import webdriver
import time
import selenium.webdriver.support.ui as ui
driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.get('https://user.nzpyq.com')
#log in
driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/form/div[1]/div[2]/div/span/input').send_keys('225851213')
# time.sleep(3)
driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/form/div[2]/div[2]/div/span/input').send_keys('111111')
# time.sleep(3)
driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/form/div[4]/div/div/span/button').click()
time.sleep(3)
#选择商户
driver.find_element_by_xpath('/html[1]/body[1]/div[1]/section[1]/aside[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[1]/a[1]').click()
driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div/div/div/ul/li[4]/div[2]/a/button').click()
#create adevertisment
time.sleep(3)
#点击添加按钮
driver.find_element_by_xpath('//div[@class="ant-list-item-meta"]//a[1]//button[1]').click()
time.sleep(3)
#create information
driver.find_element_by_xpath('/html[1]/body[1]/div[1]/section[1]/section[1]/main[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/span[1]/input[1]').send_keys('EGE')
driver.find_element_by_xpath('/html[1]/body[1]/div[1]/section[1]/section[1]/main[1]/div[1]/div[1]/form[1]/div[2]/div[2]/div[1]/span[1]/input[1]').send_keys('MEDIUM')
#选择oncall
driver.find_element_by_xpath('/html[1]/body[1]/div[1]/section[1]/section[1]/main[1]/div[1]/div[1]/form[1]/div[3]/div[2]/div[1]/span[1]/div[1]/div[1]/div[1]/div[1]').click()
driver.find_element_by_xpath('/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]').click()
time.sleep(2)
# #选择城市
driver.find_element_by_xpath("//body/div[@id='root']/section[@class='ant-layout ant-layout-has-sider']/section[@class='ant-layout']/main[@class='ant-layout-content']/div[@class='container']/div/form[@class='ant-form ant-form-inline']/div[4]/div[2]/div[1]/span[1]/div[1]/div[1]/div[1]/div[1]").click()
# time.sleep(2)

driver.find_element_by_xpath("/html/body/div[2]/div/div/div/ul/li[3]").click()
#添加地点
driver.find_element_by_xpath("//div[5]//div[2]//div[1]//span[1]//input[1]").send_keys('749841 road')
#选择zb
driver.find_element_by_xpath("//body/div[@id='root']/section[@class='ant-layout ant-layout-has-sider']/section[@class='ant-layout']/main[@class='ant-layout-content']/div[@class='container']/div/form[@class='ant-form ant-form-inline']/div[6]/div[2]/div[1]/span[1]/div[1]/div[1]/div[1]/div[1]").click()
driver.find_element_by_xpath("//li[@class='ant-select-dropdown-menu-item ant-select-dropdown-menu-item-active']").click()

#选择发色
driver.find_element_by_xpath("//body/div[@id='root']/section[@class='ant-layout ant-layout-has-sider']/section[@class='ant-layout']/main[@class='ant-layout-content']/div[@class='container']/div/form[@class='ant-form ant-form-inline']/div[7]/div[2]/div[1]/span[1]/div[1]/div[1]/div[1]/div[1]").click()
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/ul/li[1]").click()
#添加国籍
driver.find_element_by_xpath("//div[8]//div[2]//div[1]//span[1]//input[1]").send_keys("New Zealand")
#选择人群
driver.find_element_by_xpath("//body/div[@id='root']/section[@class='ant-layout ant-layout-has-sider']/section[@class='ant-layout']/main[@class='ant-layout-content']/div[@class='container']/div/form[@class='ant-form ant-form-inline']/div[9]/div[2]/div[1]/span[1]/div[1]/div[1]/div[1]/div[1]").click()
#选择语言
driver.find_element_by_xpath("//body/div[@id='root']/section[@class='ant-layout ant-layout-has-sider']/section[@class='ant-layout']/main[@class='ant-layout-content']/div[@class='container']/div/form[@class='ant-form ant-form-inline']/div[10]/div[2]/div[1]/span[1]/div[1]/div[1]/div[1]/div[1]").click()
driver.find_element_by_xpath("//li[contains(text(),'Maori')]").click()
#电话
driver.find_element_by_xpath("//div[11]//div[2]//div[1]//span[1]//input[1]").send_keys('456463')
#年龄
driver.find_element_by_xpath("//div[12]//div[2]//div[1]//span[1]//div[1]//div[2]//input[1]").send_keys('30')
#身高
driver.find_element_by_xpath("//div[13]//div[2]//div[1]//span[1]//div[1]//div[2]//input[1]").send_keys('180')
#体重
driver.find_element_by_xpath("//div[14]//div[2]//div[1]//span[1]//div[1]//div[2]//input[1]").send_keys('69')
#用户等级
driver.find_element_by_xpath("//div[15]//div[2]//div[1]//span[1]//div[1]//div[1]//div[1]").click()
driver.find_element_by_xpath("//li[contains(text(),'VIP')]").click()
#购买时间
driver.find_element_by_xpath("//div[16]//div[2]//div[1]//span[1]//div[1]//div[1]//div[1]").click()
driver.find_element_by_xpath("//li[@class='ant-select-dropdown-menu-item ant-select-dropdown-menu-item-active']").click()
time.sleep(2)
#购买价格
driver.find_element_by_xpath('/html/body/div[1]/section/section/main/div/div/form/div[17]/div[2]/div/span/div[1]/div[2]/input').send_keys('100')
driver.find_element_by_xpath('/html/body/div[1]/section/section/main/div/div/form/div[17]/div[2]/div/span/div[2]/div[2]/input').send_keys('180')
driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div/form/div[17]/div[2]/div/span/div[3]/div[2]/input').send_keys('280')

#个人介绍
driver.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div/form/div[18]/div[2]/div/span/textarea').send_keys('verfyegegd egeg')
