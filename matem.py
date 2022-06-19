from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    element = browser.find_element(By.CSS_SELECTOR, '#answer')
    element.send_keys(y)

    robot = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    robot.click()

    rule = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", rule)
    rule.click()

    button = browser.find_element(By.CSS_SELECTOR, 'body > div > form > button')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()
