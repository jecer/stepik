from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://mail.yandex.ru/?uid=156938777#inbox"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    log = 'jecer1995'
    pas = 'AndreyBondarenko1'

    login_button = browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div[4]/a[2]')
    login_button.click()

    login = browser.find_element(By.CSS_SELECTOR, '#passp-field-login').send_keys(log)
    sign_in = browser.find_element(By.CSS_SELECTOR, '#passp\:sign-in').click()

    password = browser.find_element(By.CSS_SELECTOR, '#passp-field-passwd').send_keys(pas)
    sign_in_finaly = browser.find_element(By.CSS_SELECTOR, '#passp\:sign-in').click()


    bold = browser.find_element(By.CLASS_NAME, 'mail-MessageSnippet-FromText')
    if bold.get_attribute('font-weight: bold;'):
        no_check = browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[7]/div/div[3]/div[2]/div/main/div[4]/div[2]/div/div[2]/div/div/div[1]/label/span')
        no_check.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(300)
    # закрываем браузер после всех манипуляций
    browser.quit()