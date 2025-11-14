from selenium import webdriver
import time


url = 'http://parsinger.ru/selenium/6/6.html'
with webdriver.Chrome() as browser:
    browser.install_addon('C:\Users\Filippova.Elvina.RW\AppData\Local\Google\Chrome\User Data\Profile 1\Extensions\ololmadlpnbbagpkjhdomclggmfomhdg\coordinates.crx')
    browser.get(url)
    time.sleep(500)