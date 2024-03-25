import unittest
import ddt
from loguru import logger

from Public.Common.CommonConfig import make_price_standard, CurrentTime_format_all
from Public.Common.MyLog import makeLogFile
from Public.Common.MyTestcase import MyTestCase
from Public.Common.makeErrorScreenshot import err_img
from Public.Pages.HomePage import myhome
from Public.Pages.LoginPage import mylogin
from Public.Pages.ShopCartPage import myshopcart
from time import sleep

from Public.Pages.IntroductionPage import *


@ddt.ddt
class Test_HomePage(MyTestCase):

    @classmethod
    def setUpClass(cls):
        # makeLogFile("Test_HomePage")
        cls.init_method(driver)
        myhome.delete_all_cookies()
        mylogin.login('standard_user', 'secret_sauce')

    @classmethod
    def tearDownClass(cls):
        sleep(0.5)
        # driver.quit()

    @ddt.data(*('az', 'za', 'lohi', 'hilo'))
    def test_0_range_products_and_show_in_home(self, data):
        try:
            alist = myhome.choose_range_way_and_return_sorted_list(data, make_price_standard)
            print(alist)
            sleep(2)
            real_list = myhome.get_all_product_list()
            for index, value in enumerate(real_list):
                hope_list = [alist[index]['name'], alist[index]['img_url'], alist[index]['describe'], alist[index]['price']]
                real_list = list(value.values())
                self.assertCountEqual(hope_list, real_list, "商品排序功能异常！！")
            self.log_pass()
        except AssertionError as e:
            err_img.makeErrorPng(myhome.folder_name, "商品排序与在首页展示", CurrentTime_format_all())
            raise e

    @ddt.data(*range(6))
    def test_1_enter_to_introduction_by_name_and_show_in_introduction(self, data):
        try:
            from_msg = myhome.get_chosen_product_msg(data)
            myhome.enter_introduce_pages_by_name(data)
            sleep(0.5)
            target_url = myhome.product_readyaml.read_except_data_by_key("name", from_msg['name'])['introduce_url']
            self.assert_url(target_url, None, "Back to products")
            sleep(0.5)
            last_msg = myintroduction.get_product_msg()
            self.assertEqual(from_msg, last_msg, "商品前后展示不一致！！")
            self.log_pass()
        except AssertionError as e:
            err_img.makeErrorPng(myhome.folder_name, "从名称进入详情页并展示", CurrentTime_format_all())
            self.log_fail()
            raise e
        finally:
            myintroduction.back_to_home()
            sleep(0.5)

    @ddt.data(*range(6))
    def test_2_enter_to_introduction_by_img_and_show_in_introduction(self, data):
        try:
            from_msg = myhome.get_chosen_product_msg(data)
            myhome.enter_introduce_pages_by_img(data)
            sleep(0.5)
            target_url = myhome.product_readyaml.read_except_data_by_key("name", from_msg['name'])['introduce_url']
            self.assert_url(target_url, None, "Back to products")
            last_msg = myintroduction.get_product_msg()
            self.assertEqual(from_msg, last_msg, "商品前后展示不一致！！")
            self.log_pass()
        except AssertionError as e:
            err_img.makeErrorPng(myhome.folder_name, "从图片进入详情页并展示", CurrentTime_format_all())
            self.log_fail()
            raise e
        finally:
            myintroduction.back_to_home()
            sleep(0.5)

    def test_3_from_home_add_and_show_in_shopcart(self):
        try:
            for i in range(6):
                myhome.add_to_ShopCar(i)
            sleep(0.5)
            num = int(myshopcart.shopcart_num.text)
            self.assertEqual(6, num, "购物车图标商品数量显示不正确！！！")
            hope_list = myhome.get_all_product_list()
            myshopcart.enter_shopcart()
            sleep(0.5)
            self.assert_url(myshopcart.shopcart_url, None, "Your Cart")
            real_list = myshopcart.get_shopcart_product_msg()
            for idx, val in enumerate(hope_list):
                val.pop('img_url')
            self.assertCountEqual(hope_list, real_list, "购物车商品显示异常！！！")
            self.log_pass()
        except AssertionError as e:
            self.log_fail()
            raise e

    # def test_4_from_home_remove_and_show_in_shopcart(self):
    #     try:
    #         pass
    #     except AssertionError as e:
    #         raise e
    #
    # @ddt.data(*range(6))  # 0,1,2,3,4,5
    # def test_5_from_introduction_add_and_show_in_shopcart(self, data):
    #     try:
    #         pass
    #     except AssertionError as e:
    #         raise e
    #
    # @ddt.data()
    # def test_6_from_introduction_remove_and_show_in_shopcart(self):
    #     try:
    #         pass
    #     except AssertionError as e:
    #         raise e
    #
    # @ddt.data()
    # def test_num_button_change_and_introduction_backhome(self):
    #     try:
    #         pass
    #     except AssertionError as e:
    #         raise e
    #
    # @ddt.data()
    # def test_example(self):
    #     try:
    #         pass
    #     except AssertionError as e:
    #         raise e


# if __name__ == "__main__":
#     unittest.main()
