import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class TestUniqueSelectors(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def fill_form(self, link):
        browser = self.driver
        browser.implicitly_wait(5)
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        elements = browser.find_element(By.XPATH, '//label[text()="First name*"]/following-sibling::input')
        elements2 = browser.find_element(By.XPATH, '//label[text()="Last name*"]/following-sibling::input')
        elements3 = browser.find_element(By.XPATH, '//label[text()="Email*"]/following-sibling::input')
        for element in elements, elements2, elements3:
            element.send_keys('sss')
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # ждем загрузки страницы
        sleep(1)

        welcome_text = browser.find_element(By.TAG_NAME, 'h1').text
        return welcome_text

    def test_registration(self):
        link = 'http://suninjuly.github.io/registration1.html'
        registration_result = self.fill_form(link)

        self.assertEqual("Congratulations! You have successfully registered!", registration_result)

    def test_registration_bug(self):
        link = 'http://suninjuly.github.io/registration2.html'
        registration_result = self.fill_form(link)

        self.assertEqual("Congratulations! You have successfully registered!", registration_result)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
