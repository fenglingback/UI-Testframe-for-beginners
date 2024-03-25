import unittest
import ddt
from loguru import logger

from Public.Pages.HomePage import myhome
from Public.Pages.ShopCartPage import myshopcart
from Public.Common.CommonConfig import CurrentTime_format_all
from Public.Common.MyLog import makeLogFile
from Public.Common.MyTestcase import MyTestCase
from Public.Common.makeErrorScreenshot import err_img
from Public.Pages.SidebarPage import *
from Public.Pages.LoginPage import mylogin


# @ddt.ddt
class Test_SidebarPage(MyTestCase):

    @classmethod
    def setUpClass(cls):
        # makeLogFile("Test_HomePage")
        cls.init_method(driver)
        # sidebar.delete_all_cookies()
        mylogin.login('standard_user', 'secret_sauce')

    @classmethod
    def tearDownClass(cls):
        sleep(0.5)
        # logger.stop()
        # driver.quit()

    def test_0_open_and_close(self):
        try:
            driver.refresh()
            mysidebar.control_sidebar('open')
            sleep(1)
            self.assert_style_isConform(mysidebar.sidebar_location['侧边栏'], "position: fixed; right: inherit; z-index: 1100; width: 300px; height: 100%; transition: all 0.5s ease "
                                                                           "0s;", True)
            mysidebar.control_sidebar('close')
            sleep(1)
            self.assert_style_isConform(mysidebar.sidebar_location['侧边栏'], "position: fixed; right: inherit; z-index: 1100; width: 300px; height: 100%; transition: all 0.5s ease "
                                                                           "0s; transform: translate3d(-100%, 0px, 0px);", True)
            self.log_pass()
        except AssertionError as e:
            err_img.makeErrorPng(sidebar.folder_name, sidebar.powerpoint[0], CurrentTime_format_all())
            self.log_fail()
            raise e

    def test_1_click_AllItems(self):
        try:
            driver.refresh()
            mysidebar.control_sidebar('open')
            sleep(0.5)
            mysidebar.click_AllItems()
            sleep(1)
            self.assert_url(sidebar.home_url, "Swag Labs", "Name (A to Z)")
            self.log_pass()
        except AssertionError as e:
            err_img.makeErrorPng(sidebar.folder_name, sidebar.powerpoint[1], CurrentTime_format_all())
            self.log_fail()
            raise e
        finally:
            mysidebar.back()

    def test_2_click_About(self):
        try:
            driver.refresh()
            mysidebar.control_sidebar('open')
            sleep(0.5)
            mysidebar.click_About()
            sleep(1)
            self.assert_url(sidebar.about_url, "Sauce Labs: Cross Browser Testing, Selenium Testing & Mobile Testing", "Try it free")
            self.log_pass()
        except AssertionError as e:
            err_img.makeErrorPng(sidebar.folder_name, sidebar.powerpoint[2], CurrentTime_format_all())
            self.log_fail()
            raise e
        finally:
            mysidebar.back()
            sleep(0.5)

    def test_3_click_Reset(self):
        try:
            driver.refresh()
            mysidebar.control_sidebar('open')
            sleep(0.5)
            mysidebar.click_Reset()
            sleep(0.5)
            mysidebar.control_sidebar('close')
            sleep(1)
            self.assertEqual(False, myshopcart.shopcart_num.is_exist(), "reset按钮失效！！！")
            self.assertNotIn('Remove', driver.page_source, "按钮更换功能有误！！！")
            self.log_pass()
        except AssertionError as e:
            err_img.makeErrorPng(sidebar.folder_name, sidebar.powerpoint[3], CurrentTime_format_all())
            self.log_fail()
            raise e

    def test_4_click_Logout(self):
        try:
            driver.refresh()
            mysidebar.control_sidebar('open')
            sleep(0.5)
            mysidebar.click_Logout()
            sleep(0.5)
            self.assert_url(sidebar.login_url, "Swag Labs", "performance_glitch_user")
            sleep(0.5)
            self.assert_cookie_IsExist("session-username", "standard_user", False)
            self.log_pass()
        except AssertionError as e:
            err_img.makeErrorPng(sidebar.folder_name, sidebar.powerpoint[4], CurrentTime_format_all())
            self.log_fail()
            raise e


# if __name__ == "__main__":
#     unittest.main()
