import unittest
import ddt
from loguru import logger

from Public.Common.CommonConfig import CurrentTime_format_all
from Public.Common.MyLog import makeLogFile
from Public.Common.MyTestcase import MyTestCase
from Public.Common.makeErrorScreenshot import err_img
from Public.Pages.LoginPage import *
from poium.common.logging import logging


@ddt.ddt
class Test_LoginPage(MyTestCase):

    @classmethod
    def setUpClass(cls):
        # makeLogFile("Test_LoginPage")
        cls.init_method(driver)
        mylogin.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        sleep(0.5)
        # logger.stop()
        # driver.quit()

    @ddt.data(*mylogin.right)
    def test_0_login_pass(self, data):
        try:
            mylogin.login(data[0], data[1])
            logging.info("用例说明：" + data[4])
            self.assert_url(data[2], "Swag Labs", data[3])
            self.log_pass()
        except AssertionError as e:
            err_img.makeErrorPng(mylogin.folder_name, mylogin.powerpoint[0], CurrentTime_format_all())
            self.log_fail()
            raise e
        finally:
            driver.delete_all_cookies()

    @ddt.data(*mylogin.fail)
    def test_1_login_fail(self, data):
        try:
            mylogin.login(data[0], data[1])
            logging.info("用例说明：" + data[4])
            self.assert_url(data[2], "Swag Labs", data[3])
            logging.info("测试通过！！")
        except AssertionError as e:
            err_img.makeErrorPng(mylogin.folder_name, mylogin.powerpoint[0], CurrentTime_format_all())
            raise e

    # def test_2_cookie(self):
    #     try:
    #         mylogin.login('standard_user', 'secret_sauce')
    #         self.assert_cookie_IsExist("session-username", "standard_user", True)
    #     except AssertionError as e:
    #         raise e


# if __name__ == "__main__":
#     unittest.main()
