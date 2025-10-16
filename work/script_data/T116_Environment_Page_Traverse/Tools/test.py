import time

from selenium import webdriver
from selenium.webdriver.common.by import By



username_input = "#login_username"
password_input = "#login_password"

login_button = "button[class='css-1e9l0kj ant-btn ant-btn-primary login-submit'] span"
login_success_prompt = '.flex.items-end.font-600.text-20px.inline-flex.leading-20px'


driver = webdriver.Edge()

driver.maximize_window()

url = "http://test1erp.50bm.cc/#/login"  # test1环境

driver.get(url)

time.sleep(2)
driver.find_element(By.CSS_SELECTOR, username_input).send_keys('BM002971')
driver.find_element(By.CSS_SELECTOR, password_input).send_keys('883304yoyo')
driver.find_element(By.CSS_SELECTOR, login_button).click()
time.sleep(3)


driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > section:nth-child(1) > header:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "[data-submenu-id='/workflow']").click()

time.sleep(2)





