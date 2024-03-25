import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class testCommon(unittest.TestCase):
    hh_url = "https://www.saucedemo.com/"
    test_loc = (By.XPATH, '//*[@id="anticc_vcode"]/body/div/div/div[3]/form/div/div[1]/span/img')

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(cls.hh_url)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        pass

    def test_Element(self):
        driver = self.driver
        try:
            # driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
            # driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
            # driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
            driver.add_cookie(
                {'name': 'session-username', 'value': 'standard_user', 'expiry': 1716783170})
            sleep(1)
            print(driver.get_cookies())
            driver.refresh()
        except Exception as e:
            # 有待完善
            # makeScreenShot(driver).makeErrorPng("测试账户登录功能错误")
            raise e


if __name__ == '__main__':
    unittest.main()
