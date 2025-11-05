from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#1
#
# url = 'http://parsinger.ru/selenium/3/3.html'
# browser = webdriver.Chrome()
# browser.get(url)
# elem = browser.find_element(By.CLASS_NAME, 'text')
# print(elem)
# time.sleep(2)
# browser.quit()

#2
# url = 'https://parsinger.ru/selenium/3/3.2.1/index.html'
# browser = webdriver.Chrome()
# browser.get(url)
# browser.find_element(By.ID, "clickButton").click()
#
# time.sleep(3)
# print(browser.find_element(By.ID, "codeOutput").text)
# time.sleep(20)
# browser.quit()

#3
# url = "https://parsinger.ru/selenium/3/3.2.2/index.html"
# browser = webdriver.Chrome()
# browser.get(url)
# browser.find_element(By.ID, "codeInput").send_keys("Дрогон")
# time.sleep(3)
# browser.find_element(By.ID, "clickButton").click()
# print(browser.find_element(By.ID, "codeOutput").text)
# time.sleep(10)
# browser.quit()


#4
# url = "https://parsinger.ru/selenium/3/3.2.3/index.html"
# browser = webdriver.Chrome()
# browser.get(url)
# browser.find_element(By.ID, "showTextBtn").click()
# password = browser.find_element(By.ID, "text1").text
# time.sleep(0.5)
# browser.find_element(By.ID, "userInput").send_keys(password)
# time.sleep(0.5)
# browser.find_element(By.ID, "checkBtn").click()
# print(browser.find_element(By.ID,"text2").text)
# time.sleep(5)
# browser.quit()


#5
# url = "https://parsinger.ru/selenium/3/3.2.4/index.html"
# browser = webdriver.Chrome()
# browser.get(url)
# time.sleep(5)
# browser.find_element(By.ID, "secret-key-button").click()
# time.sleep(5)
# link = browser.find_element(By.ID, "secret-key-button").get_attribute("data")
# time.sleep(5)
# print(link)
#
# browser.quit()

# #6
# url = "https://parsinger.ru/selenium/3/3.3.3/index.html"
# browser = webdriver.Chrome()
# browser.get(url)
# time.sleep(5)
# browser.find_element(By.ID, "linksContainer").click()
#
# time.sleep(5)
# browser.quit()

#7 Каскадный поиск
url = "https://parsinger.ru/selenium/3/3.3.1/index.html"
browser = webdriver.Chrome()
browser.get(url)
time.sleep(2)
parent = browser.find_element(By.ID, "parent_id")
child = parent.find_element(By.CLASS_NAME, "child_class")
child.click()
time.sleep(2)
password = child.get_attribute("password")
print(password)
browser.quit()