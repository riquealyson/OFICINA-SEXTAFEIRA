from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


service = Service(ChromeDriverManager().install())

browser = webdriver.Chrome(service=service)

browser.get('https://www.google.com.br')

search_input = browser.find_element(By.NAME, 'q')

search_input.send_keys('Porto Digital')

search_input.send_keys(Keys.RETURN)

sleep(20)