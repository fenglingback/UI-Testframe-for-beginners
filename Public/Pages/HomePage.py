from time import sleep

from Public.Common.father import driver
from Public.Pages.BasePage import basePage
from Data.Elements_and_Data import home
import copy


class Home(basePage, home):

    def __init__(self, mydriver):
        self.driver = mydriver
        self.hooks_func = None

    def register_hook(self, hook_func):
        self.hooks_func = hook_func

    def choose_range_way_and_return_sorted_list(self, way, unite_func=None) -> list:
        """

        :param way: 只有四种排序方式----①az：Name (A to Z)；②za：Name (Z to A)；③lohi：Price (low to high)；④hilo：Price (high to low)
        :param unite_func:
        :return:
        """
        templist = []
        if way == 'az':
            data = copy.deepcopy(self.product_data)
            self.range_loc.select_by_value(way)
            templist = sorted(data, key=lambda x: x['name'])
        elif way == 'za':
            data = copy.deepcopy(self.product_data)
            self.range_loc.select_by_value(way)
            templist = sorted(data, key=lambda x: x['name'], reverse=True)
        elif way == 'lohi':
            data = copy.deepcopy(self.product_data)
            self.range_loc.select_by_value(way)
            templist = sorted(data, key=lambda x: x['price'])
        elif way == 'hilo':
            data = copy.deepcopy(self.product_data)
            self.range_loc.select_by_value(way)
            templist = sorted(data, key=lambda x: x['price'], reverse=True)
        # else:
        #     raise Exception("排序方式书写有误！！！")

        # 先注册钩子函数，再执行该函数
        if self.hooks_func is None and unite_func is not None:
            self.register_hook(unite_func)

        if self.hooks_func is not None:
            templist2 = copy.deepcopy(templist)
            templist2 = self.hooks_func(templist2)
            return templist2

        return templist

    '''
    '''

    def get_chosen_product_msg(self, index) -> dict:
        """

        :param index:
        :return: 依次返回商品的名称、图片链接、描述、价格
        """
        img_url = self.img[index].get_attribute('src')
        name = self.name[index].text
        describe = self.describe[index].text
        price = self.price[index].text
        msg = {'name': name, 'img_url': img_url, 'describe': describe, 'price': price}
        return msg

    '''
    '''

    def get_all_product_list(self) -> list:

        last_list = []
        for i in range(len(self.img)):
            msg = self.get_chosen_product_msg(i)
            last_list.append(msg)

        return last_list

    '''
    '''

    def enter_introduce_pages_by_name(self, index):
        """
        从名称处进入详情页
        :param index: 从 0 开始选择进入的商品链接
        :return:
        """
        self.name_a[index].click()

    '''
    '''

    def enter_introduce_pages_by_img(self, index):
        """
        从图片处进入详情页
        :param index: 从 0 开始选择进入的商品链接
        :return:
        """
        self.img_a[index].click()

    '''
    '''

    def add_to_ShopCar(self, index):
        """
        添加至购物车
        :param index:
        :return:
        """

        self.add_and_remove_button[index].click()

    '''
    '''

    def remove_from_ShopCar(self, index):
        """
        从购物车移除
        :param index:
        :return:
        """
        self.add_and_remove_button[index].click()


myhome = Home(driver)
