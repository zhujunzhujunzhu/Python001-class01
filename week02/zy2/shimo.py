'''
@Description 
@Autor 朱俊
@Date 2020-07-05 20:28:51
@LastEditors 朱俊
@LastEditTime 2020-07-05 20:55:12
'''

'''
使用 requests 或 Selenium 模拟登录石墨文档 https://shimo.im
'''

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://shimo.im')  # 进入到石墨文档
time.sleep(2)
try:
    driver.find_element_by_class_name("login-button").click()
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys("")
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys("")
    time.sleep(2)
    driver.find_element_by_class_name('submit').click()
    # 拿到登录后的cookies
    cookies = driver.get_cookies()
except Exception as e:
    print(e)

finally:
    time.sleep(15)
    driver.close()
